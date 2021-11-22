import csv
from django.http import request
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required


 
# Create your views here.

# @login_required
def base(request):
    title='Welcome:Stock management'
    form="welcome"
    context={
        "title":title,
        "test":form
       }
    return render (request,'base.html',context)

# @login_required
def list_item(request):
    header='Stock'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form":form
    }
    
    if request.method == 'POST':
        queryset = Stock.objects.filter(
            # category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
            )
     
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

        context = {
            "form": form,
            "header": 'header',
            "queryset": queryset,
                  }
    return render(request, "list_item.html", context)
# @login_required
def add_items(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/stock/list_item')
    context={
        "form":form,
        "title":'Additems',
        }
    return render(request,"add_items.html",context)
    
# @login_required
def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/stock/list_item')
    context = {
        'form':form
	}
    return render(request, 'update_items.html', context)

# @login_required
def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)



# @login_required
def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "request.html", context)


# @login_required
def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Receive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "receive.html", context)

# @login_required
def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))

		return redirect("/stock/list_item")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_items.html", context)

    
# Requesting for menu
# @login_required
def menu_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock/stock_detail/'+str(instance.id))
		

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "request.html", context)


# # ADD MENU
# @login_required
def add_menu(request):
    form=AddMenu(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/stock/menu')
    context={
        "form":form,
        "title":'Additems',
        }
    return render(request,"add_menu.html",context)




# @login_required
def menu(request):
    header='Menu'
    form = MenuSearchForm(request.POST or None)
    queryset = Menu.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form":form
    }
    
    if request.method == 'POST':
        queryset = Menu.objects.filter(
            # category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
            )
     
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Menu.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for menu in instance:
                writer.writerow([menu.category, menu.item_name, menu.quantity])
            return response

        context = {
            "form": form,
            "header": 'header',
            "queryset": queryset,
                  }
    return render(request, "menu.html", context)



# @login_required
def update_menu(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/stock/menu')
    context = {
        'form':form
	}
    return render(request, 'add_menu.html', context)