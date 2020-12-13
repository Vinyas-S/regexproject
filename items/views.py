from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Item, Category, Price
from .forms import SignUp
# Create your views here.

@login_required
def home(request):
	items_list = Item.objects.all()

	page = request.GET.get('page', 1)

	paginator = Paginator(items_list, 10)
	try:
		items = paginator.page(page)		
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	return render(request, 'items/items_list.html', {'items':items})


def sign_up(request):
	if request.method == 'POST':
		form = SignUp(request.POST)
		if not form.is_valid():
			# form = SignUp()
			return render(request, 'sign_up.html', {'form':form})

		else:
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, password=password)
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/items/')
	else:
		return render( request, 'sign_up.html', {'form': SignUp()})


