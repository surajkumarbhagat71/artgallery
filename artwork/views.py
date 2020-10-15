from django.shortcuts import render,redirect
from django.db.models import Q
from .models import *
from .forms import *

# Create your views here.

def home(r):

    return render(r,'home.html')


def p_product(r):

    data = {"p_product":Product.objects.all()}

    return render(r,'public_product.html',data)




############################################  Owner #######################################

def login(r):
    if r.method == "POST":
        username = r.POST.get('username')
        password = r.POST.get('password')

        cond = Q(email = username) & Q(password = password)

        cheak = Oner.objects.filter(cond).count()

        if (cheak > 0):
            r.session["login"] = username
            return redirect(oner_profile)
        else:
            return redirect(login)

    return render(r,'oner/login.html')

def all_painting(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {"painting":Product.objects.all()}

    return render(r,'oner/all_painting.html',data)



def oner_dashabord(r):
    if not r.session.has_key('login'):
        return redirect(login)
    data = {
        "order":Order.objects.all().count(),
        "product":Product.objects.all().count(),
        "user":User.objects.all().count()
    }

    return render(r,'oner/dashabord.html',data)


def add_panting(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = ProductForm(r.POST or None , r.FILES or None)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(oner_dashabord)

    data = {"pform":form}

    return render(r,'oner/add_panting.html',data)


def all_order(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {"order":Order.objects.all()}

    return render(r,'oner/all_order.html',data)


def oner_profile(r):
    if not r.session.has_key('login'):
        return redirect(login)

    id = Oner.objects.get(email=r.session['login']).oner_id

    data = {"profile":Oner.objects.get(oner_id = id)}

    return render(r,'oner/profile.html',data)


def delete_product(r,id):
    if not r.session.has_key('login'):
        return redirect(login)

    data = Product.objects.filter(pro_id=id)
    data.delete()
    return render(r,'oner/all_painting.html')

#######################################################################################################

def edit(r,pro_id):
    get_id = Product.objects.get(pro_id=pro_id)

    a = ProductForm(r.POST or None , r.FILES or None , instance=get_id)

    if r.method == "POST":
        if a.is_valid():
            a.save()
            return redirect(all_painting)

    data = {"eform":a}

    return render(r,'oner/edit_product.html',data)


def oner_logout(r):
    if r.session.has_key('login'):
        del r.session['login']


    return render(r,'home.html')


###################################################  User ##########################################

def signup(r):
    form = UserForm(r.POST or None ,r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(ulogin)

    data = {"form":form}

    return render(r,'user/signup.html',data)


def ulogin(r):
    if r.method == "POST":
        username = r.POST.get('username')
        password = r.POST.get('password')

        cond = Q(email = username) & Q(password = password)

        cheak = User.objects.filter(cond).count()

        if (cheak > 0):
            r.session["ulogin"] = username
            return redirect(profile)
        else:
            return redirect(ulogin)

    return render(r,'user/ulogin.html')



def my_order(r):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)

    id = User.objects.get(email = r.session['ulogin']).user_id

    data = {"my_order":Order.objects.filter(user_id = id).order_by('-order_time')}

    return render(r,'user/my_order.html',data)


def product(r):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)

    data = {"product":Product.objects.all()}

    return render(r,'user/product.html',data)


def profile(r):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)

    id = User.objects.get(email = r.session['ulogin']).user_id

    data = {"user":User.objects.get(user_id = id )}

    return render(r,'user/profile.html',data)

def order(r,id):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)

    o_id = User.objects.get(email = r.session['ulogin']).user_id

    b = Order()
    b.user_id = User(o_id)
    b.pro_id = Product(id)
    b.save()
    return redirect(my_order)

    return render(r,'user/my_order.html')


def edit_profile(r,id):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)
    get_id = User.objects.get(user_id=id)

    form = UserForm(r.POST or None , r.FILES or None , instance= get_id)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(profile)

    data = {"pform":form}

    return render(r,'user/edit_profile.html',data)

def delete_order(r,id):
    if not r.session.has_key('ulogin'):
        return redirect(ulogin)

    data = Order.objects.filter(order_id = id)

    data.delete()
    return render(r,'user/my_order.html')


def logout(r):
    if r.session.has_key('ulogin'):
        del r.session['ulogin']
        return redirect(ulogin)

    return render(r,'home.html')



def about(r):

    return render(r,'oner/about.html')


