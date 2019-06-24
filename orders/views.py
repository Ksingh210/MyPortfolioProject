from django.shortcuts import render
from .forms import Orderform

def orderdetails(request):

    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save(commit=True)

    form = Orderform()

    return render(request,'orders/order_requests.html',{'form':form})
