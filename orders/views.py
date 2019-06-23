from django.shortcuts import render

def orderrequest(request):
    return render(request, 'orders/order_requests.html')

def ordersubmitted(request):

    storeorder = request.GET['store_number']

    item1 = request.GET.get('soil1')
    soil1pallets = request.GET['soil1pallets']

    item2 = request.GET.get('soil2')
    soil2pallets = request.GET['soil2pallets']

    item3 = request.GET.get('soil3')
    soil3pallets = request.GET['soil3pallets']


    return render(request, 'orders/ordersubmitted.html',
                  {'store': storeorder,
                   'item1': item1,
                   'item2': item2,
                   'item3': item3,
                   'soil1pallets': soil1pallets,
                   'soil2pallets': soil2pallets,
                   'soil3pallets': soil3pallets,})




