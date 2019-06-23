from django.shortcuts import render

def orderrequest(request):
    return render(request, 'orders/order_requests.html')

def ordersubmitted(request):
    order_placed = {}

    order_placed.update({'Store':request.GET['store_number']})
    order_placed.update({request.GET.get('soil1'): (request.GET['soil1pallets'] + ' pallets')})
    order_placed.update({request.GET.get('soil2'): (request.GET['soil2pallets'] + ' pallets')})
    order_placed.update({request.GET.get('soil3'): (request.GET['soil3pallets'] + ' pallets')})

    return render(request,'orders/ordersubmitted.html',{'order_placed':order_placed})
