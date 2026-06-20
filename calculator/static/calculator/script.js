function setResult(id, message) {
    document.getElementById(id).innerText = message;
}

function showCalculator(type) {
    const sections = [
        "basicSection",
        "scientificSection",
        "bmiSection",
        "emiSection",
        "discountSection",
        "ageSection",
        "interestSection",
        "sipSection"
    ];

    const buttons = [
        "basicBtn",
        "scientificBtn",
        "bmiBtn",
        "emiBtn",
        "discountBtn",
        "ageBtn",
        "interestBtn",
        "sipBtn"
    ];

    document.getElementById("welcomeCard").style.display = "none";

    sections.forEach(id => {
        document.getElementById(id).classList.remove("active-section");
    });

    buttons.forEach(id => {
        document.getElementById(id).classList.remove("active");
    });

    document.getElementById(type + "Section").classList.add("active-section");
    document.getElementById(type + "Btn").classList.add("active");

    localStorage.setItem("selectedCalculator", type);
}

window.onload = function () {
    const selectedCalculator = localStorage.getItem("selectedCalculator");

    if (selectedCalculator) {
        showCalculator(selectedCalculator);
    }
};

function reloadAfterCalculation() {
    setTimeout(() => {
        location.reload();
    }, 900);
}

function appendValue(value) {
    document.getElementById("expression").value += value;
}

function clearExpression() {
    document.getElementById("expression").value = "";
    setResult("basicResult", "Result will appear here");
}

function deleteLast() {
    const input = document.getElementById("expression");
    input.value = input.value.slice(0, -1);
}

function calculateBasic() {
    const expression = document.getElementById("expression").value;

    fetch(`/calculate/?expression=${encodeURIComponent(expression)}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult("basicResult", "Result: " + data.result);
                reloadAfterCalculation();
            } else {
                setResult("basicResult", "Error: " + data.error);
            }
        });
}

function calculateScientific() {
    const value = document.getElementById("scientificValue").value;
    const operation = document.getElementById("operation").value;

    fetch(`/scientific/?operation=${operation}&value=${value}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult("scientificResult", "Result: " + data.result);
                reloadAfterCalculation();
            } else {
                setResult("scientificResult", "Error: " + data.error);
            }
        });
}

function calculateBMI() {
    const weight = document.getElementById("weight").value;
    const height = document.getElementById("height").value;

    fetch(`/bmi/?weight=${weight}&height=${height}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult("bmiResult", `BMI: ${data.result} | Status: ${data.status}`);
                reloadAfterCalculation();
            } else {
                setResult("bmiResult", "Error: " + data.error);
            }
        });
}

function calculateEMI() {
    const principal = document.getElementById("principal").value;
    const rate = document.getElementById("rate").value;
    const months = document.getElementById("months").value;

    fetch(`/emi/?principal=${principal}&rate=${rate}&months=${months}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult(
                    "emiResult",
                    `Monthly EMI: ₹${data.emi} | Interest: ₹${data.total_interest}`
                );
                reloadAfterCalculation();
            } else {
                setResult("emiResult", "Error: " + data.error);
            }
        });
}

function calculateDiscount() {
    const price = document.getElementById("price").value;
    const discount = document.getElementById("discountPercent").value;

    fetch(`/discount/?price=${price}&discount=${discount}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult(
                    "discountResult",
                    `Discount: ₹${data.discount_amount} | Final Price: ₹${data.final_price}`
                );
                reloadAfterCalculation();
            } else {
                setResult("discountResult", "Error: " + data.error);
            }
        });
}

function calculateAge() {
    const day = document.getElementById("birthDay").value;
    const month = document.getElementById("birthMonth").value;
    const year = document.getElementById("birthYear").value;

    fetch(`/age/?day=${day}&month=${month}&year=${year}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult("ageResult", `Your Age: ${data.age} years`);
                reloadAfterCalculation();
            } else {
                setResult("ageResult", "Error: " + data.error);
            }
        });
}

function calculateInterest() {
    const principal = document.getElementById("interestPrincipal").value;
    const rate = document.getElementById("interestRate").value;
    const time = document.getElementById("interestTime").value;
    const timeType = document.getElementById("interestTimeType").value;

    fetch(`/interest/?principal=${principal}&rate=${rate}&time=${time}&time_type=${timeType}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult(
                    "interestResult",
                    `Interest: ₹${data.total_interest} | Total: ₹${data.total_amount} | Per Day: ₹${data.daily_interest} | Per Month: ₹${data.monthly_interest}`
                );
                reloadAfterCalculation();
            } else {
                setResult("interestResult", "Error: " + data.error);
            }
        });
}

function calculateSIP() {
    const monthly = document.getElementById("sipAmount").value;
    const rate = document.getElementById("sipRate").value;
    const years = document.getElementById("sipYears").value;

    fetch(`/sip/?monthly=${monthly}&rate=${rate}&years=${years}`)
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                setResult(
                    "sipResult",
                    `Invested: ₹${data.total_invested} | Wealth Gain: ₹${data.wealth_gain} | Maturity Amount: ₹${data.maturity_amount}`
                );
                reloadAfterCalculation();
            } else {
                setResult("sipResult", "Error: " + data.error);
            }
        });
}

function clearHistory() {
    fetch("/clear-history/")
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                localStorage.removeItem("selectedCalculator");
                location.reload();
            }
        });
}