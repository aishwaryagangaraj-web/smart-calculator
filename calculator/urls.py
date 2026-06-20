from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("calculate/", views.calculate, name="calculate"),
    path("scientific/", views.scientific, name="scientific"),
    path("bmi/", views.bmi, name="bmi"),
    path("emi/", views.emi, name="emi"),
    path("discount/", views.discount, name="discount"),
    path("age/", views.age, name="age"),
    path("interest/", views.interest, name="interest"),
    path("sip/", views.sip, name="sip"),
    path("clear-history/", views.clear_history, name="clear_history"),
]