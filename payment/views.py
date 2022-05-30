from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from payment.models import Payment
from .forms import  PaymentForm



def pay(request):
   
    form=PaymentForm()
    if request.method =='POST':
        add_payment=PaymentForm(request.POST)
        if add_payment.is_valid():
            payment = add_payment.save()
            # return redirect('conformation')
            return conformation(request, payment.id)

    context={'form':form,
             'pay':pay,
             }

    return render(request,"payment/credit_card.html",context)


def conformation(request, pay_id):
    pay = Payment.objects.get(id=pay_id)
    context={
             'pay':pay,
             }
    return render(request,"payment/conformation.html",context)


def update(request, id): 
    payment_id = Payment.objects.get(id=id)
    if request.method == 'POST' :
        pay_save = PaymentForm(request.POST,instance=payment_id)
        if pay_save.is_valid():
            pay_save.save()
            return redirect('congrats')
            
    else:
        pay_save =PaymentForm(instance=payment_id)        
            
            
    context ={"form":pay_save}
    
        
    return render(request,"payment/update.html",context)

def delete(request, id):
    pay_delete = get_object_or_404(Payment, id=id) #same as .objects.get(id=id)
    if request.method == 'POST' :
        pay_delete.delete()
        return redirect('main')
    return render(request, "payment/delete.html")
        
    
    

def congrats(request):
    return render(request, "payment/congrats.html")
    
