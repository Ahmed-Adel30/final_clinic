from django.shortcuts import render
from .forms import  PaymentForm


def pay(request):
    form=PaymentForm()
    if request.method=='POST':
        add_payment=PaymentForm(request.POST)
        if add_payment.is_valid():
            add_payment.save()

    context={'form':form}

    return render(request,"payment/credit_card.html",context)
