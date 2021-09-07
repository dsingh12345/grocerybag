from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import grocerylist,login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm

# Create your views here.
def index(request):
    grocerylist1 = grocerylist.objects.all().order_by("-date")
    if request.user.is_anonymous:
        messages.error(request, 'signIn first.')
        return redirect('/signin')
    return render(request,'index.html',{'grocerylist1':grocerylist1})

# def listdate(request):
#     if request.method =='POST':
#         date = request.POST.get('date')
#         g2 = grocerylist.objects.all().filter( date =datetime.date("date"))
#         print(g2)
#         if request.user.is_anonymous:
#             return redirect('/signin')
#     return render(request,'index.html',{'grocerylist2':g2})

def add(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            name = request.POST.get('itemname')
            itemquantity = request.POST.get('itemquantity')
            status = request.POST.get('status')
            date = request.POST.get('date')
            g1 = grocerylist.objects.create(name = name,itemquantity = itemquantity,status = status, date=date)
            return redirect('/')

            
        else :
            messages.error(request, 'signIn First.')
            return redirect('/signin')
            
    return render(request,'add.html')

def update(request,grocerylist_id):
    if request.method =='POST':
        if request.user.is_authenticated:
            ins = grocerylist.objects.get(id=grocerylist_id)
            def get_object(self):
                return self.request.ins
        # ins.name = request.POST.get('itemname')
        # ins.itemquantity = request.POST.get('itemquantity')
        # ins.status = request.POST.get('status')
        # ins.date = request.POST.get('date')
        # ins.save()
            return render(request,'update.html',{'ins':ins})
            
        else :
            return redirect('/signin')
            
    return redirect('/')
    
def newlist(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            idn = request.POST.get('idno')
            name = request.POST.get('itemname')
            itemquantity = request.POST.get('itemquantity')
            status = request.POST.get('status')
            date = request.POST.get('date')
            g1 = grocerylist(id = idn ,name = name,itemquantity = itemquantity,status = status, date=date)
            g1.save()
            messages.success(request, 'updated successfully.')
            return redirect('/')
            
        else :
            return redirect('/signin')
            
    return redirect('/')

def signup(request):
    form = NewUserForm()
    context={"form":form}
    if request.method == "POST":
        form = NewUserForm (request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'signup.html', {"form":form})
    # if request.method =="POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('emailid')
    #     password = request.POST.get('password')
    #     phone = request.POST.get('phone')
    #     user = User.objects.create_user(name, email, password)


def signin(request):
    if request.method == 'POST':
       name=request.POST.get('name')
       password = request.POST.get('password')
        #    login1 = login(name=name,password=password)
        #    login1.save()
       user = authenticate(username=name, password=password)
       if user is not None:
           login(request,user)
           messages.success(request, 'signIn successfully.')
           return redirect('/')
       else:
           messages.error(request,"Invalid username or password.")
           return render(request,'signin.html')
    return render(request,'signin.html')

