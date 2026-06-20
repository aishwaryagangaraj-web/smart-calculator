import ast
import math
import operator
from datetime import date

from django.http import JsonResponse
from django.shortcuts import render

from .models import CalculationHistory


ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        op_type = type(node.op)

        if op_type not in ALLOWED_OPERATORS:
            raise ValueError

        return ALLOWED_OPERATORS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        value = safe_eval(node.operand)
        op_type = type(node.op)

        if op_type not in ALLOWED_OPERATORS:
            raise ValueError

        return ALLOWED_OPERATORS[op_type](value)

    raise ValueError


def save_history(category, expression, result):
    CalculationHistory.objects.create(
        category=category,
        expression=expression,
        result=str(result)
    )


def index(request):
    history = CalculationHistory.objects.all()[:12]
    return render(request, "calculator/index.html", {"history": history})


def calculate(request):
    try:
        expression = request.GET.get("expression", "").strip()
        expression = expression.replace("^", "**")

        tree = ast.parse(expression, mode="eval")
        result = round(safe_eval(tree.body), 6)

        save_history("Basic", expression, result)

        return JsonResponse({"success": True, "result": result})

    except ZeroDivisionError:
        return JsonResponse({"success": False, "error": "Division by zero not allowed"})

    except Exception:
        return JsonResponse({"success": False, "error": "Invalid expression"})


def scientific(request):
    try:
        operation = request.GET.get("operation")
        value = float(request.GET.get("value", 0))

        if operation == "sqrt":
            result = math.sqrt(value)
            expression = f"√{value}"
        elif operation == "sin":
            result = math.sin(math.radians(value))
            expression = f"sin({value})"
        elif operation == "cos":
            result = math.cos(math.radians(value))
            expression = f"cos({value})"
        elif operation == "tan":
            result = math.tan(math.radians(value))
            expression = f"tan({value})"
        elif operation == "log":
            result = math.log10(value)
            expression = f"log({value})"
        else:
            raise ValueError

        result = round(result, 6)
        save_history("Scientific", expression, result)

        return JsonResponse({"success": True, "result": result})

    except Exception:
        return JsonResponse({"success": False, "error": "Invalid scientific input"})


def bmi(request):
    try:
        weight = float(request.GET.get("weight", 0))
        height_cm = float(request.GET.get("height", 0))

        height_m = height_cm / 100
        result = round(weight / (height_m * height_m), 2)

        if result < 18.5:
            status = "Underweight"
        elif result < 25:
            status = "Normal"
        elif result < 30:
            status = "Overweight"
        else:
            status = "Obese"

        save_history("BMI", f"{weight}kg, {height_cm}cm", f"{result} - {status}")

        return JsonResponse({"success": True, "result": result, "status": status})

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid weight and height"})


def emi(request):
    try:
        principal = float(request.GET.get("principal", 0))
        annual_rate = float(request.GET.get("rate", 0))
        months = int(request.GET.get("months", 0))

        monthly_rate = annual_rate / 12 / 100

        if monthly_rate == 0:
            emi_value = principal / months
        else:
            emi_value = (
                principal * monthly_rate * ((1 + monthly_rate) ** months)
                / (((1 + monthly_rate) ** months) - 1)
            )

        emi_value = round(emi_value, 2)
        total_payment = round(emi_value * months, 2)
        total_interest = round(total_payment - principal, 2)

        save_history("EMI", f"₹{principal}, {annual_rate}%, {months} months", f"₹{emi_value}")

        return JsonResponse({
            "success": True,
            "emi": emi_value,
            "total_payment": total_payment,
            "total_interest": total_interest,
        })

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid loan details"})


def discount(request):
    try:
        price = float(request.GET.get("price", 0))
        discount_percent = float(request.GET.get("discount", 0))

        discount_amount = round((price * discount_percent) / 100, 2)
        final_price = round(price - discount_amount, 2)

        save_history(
            "Discount",
            f"Price ₹{price}, Discount {discount_percent}%",
            f"Final ₹{final_price}"
        )

        return JsonResponse({
            "success": True,
            "discount_amount": discount_amount,
            "final_price": final_price,
        })

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid discount details"})


def age(request):
    try:
        birth_day = int(request.GET.get("day", 0))
        birth_month = int(request.GET.get("month", 0))
        birth_year = int(request.GET.get("year", 0))

        birth_date = date(birth_year, birth_month, birth_day)
        today = date.today()

        age_years = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        save_history("Age", str(birth_date), f"{age_years} years")

        return JsonResponse({"success": True, "age": age_years})

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid date of birth"})


def interest(request):
    try:
        principal = float(request.GET.get("principal", 0))
        rate = float(request.GET.get("rate", 0))
        time_value = float(request.GET.get("time", 0))
        time_type = request.GET.get("time_type", "years")

        if time_type == "days":
            time_in_years = time_value / 365
        elif time_type == "months":
            time_in_years = time_value / 12
        else:
            time_in_years = time_value

        total_interest = round((principal * rate * time_in_years) / 100, 2)
        total_amount = round(principal + total_interest, 2)
        daily_interest = round((principal * rate) / (100 * 365), 2)
        monthly_interest = round((principal * rate) / (100 * 12), 2)

        save_history(
            "Interest",
            f"₹{principal}, {rate}%, {time_value} {time_type}",
            f"₹{total_interest}"
        )

        return JsonResponse({
            "success": True,
            "total_interest": total_interest,
            "total_amount": total_amount,
            "daily_interest": daily_interest,
            "monthly_interest": monthly_interest,
        })

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid interest details"})


def sip(request):
    try:
        monthly = float(request.GET.get("monthly", 0))
        rate = float(request.GET.get("rate", 0))
        years = int(request.GET.get("years", 0))

        monthly_rate = rate / 12 / 100
        months = years * 12

        maturity = monthly * (
            (((1 + monthly_rate) ** months) - 1) / monthly_rate
        ) * (1 + monthly_rate)

        maturity = round(maturity, 2)
        invested = round(monthly * months, 2)
        wealth_gain = round(maturity - invested, 2)

        save_history(
            "SIP",
            f"₹{monthly}/month, {rate}%, {years} years",
            f"₹{maturity}"
        )

        return JsonResponse({
            "success": True,
            "total_invested": invested,
            "wealth_gain": wealth_gain,
            "maturity_amount": maturity,
        })

    except Exception:
        return JsonResponse({"success": False, "error": "Enter valid SIP details"})


def clear_history(request):
    CalculationHistory.objects.all().delete()
    return JsonResponse({"success": True})