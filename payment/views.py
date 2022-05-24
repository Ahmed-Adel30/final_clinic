from django.shortcuts import render

def pay(request):
    return render(request,"payment/credit_card.html")
