import csv
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from store.forms import StoreCreateForm, StoreSearchForm
from django.views import View
from store.models.orders import Order
from store.models.product import Product

class OrderView(View):
    def get(self,request):
        orders = Order.objects.all()
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})


    # def get(self , request ):
    #     customer = request.session.get('customer')
    #     orders = Order.get_orders_by_customer(customer)
    #     print(orders)
    #     return render(request , 'orders.html'  , {'orders' : orders})

    def store_list(self , request ):
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        print(order)
        return render(request , 'store.html'  , {'order' : order})
    
def add_stock(request):
    form=StoreCreateForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/store')
    context={
        "form":form,
        "title":'Additems',
        }
    return render(request,"add_stock.html",context)

# def store_list(request):
#     header='Store'
#     form = StoreCreateForm(request.POST or None)
#     queryset = Product.objects.all()
#     context = {
#         "header": header,
#         "queryset": queryset,
#         "form":form
#     }
    
#     if request.method == 'POST':
#         queryset = Product.objects.filter(
#             item_name__icontains=form['name'].value()
#             )
     
#         if form['export_to_CSV'].value() == True:
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
#             writer = csv.writer(response)
#             writer.writerow(['CATEGORY', 'NAME', 'QUANTITY'])
#             instance = queryset
#             for product in instance:
#                 writer.writerow([product.category, product.name, product.quantity])
#             return response

#         context = {
#             "form": form,
#             "header": 'header',
#             "queryset": queryset,
#                   }
#     return render(request,"store.html", context)
# @login_required
