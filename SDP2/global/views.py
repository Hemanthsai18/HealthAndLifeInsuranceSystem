
from os import name
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Health_Insurance
from .models import Life_Insurance,User_Own,Details
# Create your views here.
from django.http import HttpResponse
import datetime

def profile2(request):
    return render(request,"profile2.html")
def general(request):
    return render(request,"cal_general.html")
def heart(request):
    return render(request,"cal_heart.html")
def cancer(request):
    return render(request,"cal_cancer.html")
def term(request):
    return render(request,"cal_pension.html")
def pension(request):
    return render(request,"cal_pension.html")
def endownment(request):
    return render(request,"cal_pension.html")
def blog_single(request):
    return render(request,"blog-single.html")
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")
def index_2(request):
    return render(request,"index-2.html")
def portfolio_details(request):
    return render(request,"portfolio-details.html")
def portfolio(request):
    return render(request,"portfolio.html")
def health(request):
    insure = Health_Insurance.objects.all()
    return render(request, "services.html",{'insure' : insure, 't' : True})
def life(request):
    insure = Life_Insurance.objects.all()
    return render(request, "services.html",{'insure' : insure, 't' : False})


def buy(request):
    age = request.session['age']
    amount = request.session['amount']
    year = request.session['year']
    typo = request.session['typo']
    total = request.session['total']
    name = request.POST['name']
    return render(request,"profile.html",{'age':age,'amount':amount})

def term_calculation(request):
    if request.method=="GET":
        name = "Cancer Insurance"
        age = int(request.GET['age'])
        amount = int(request.GET['amount'])
        year = request.GET['year']
        year=year.split("+")
        typo = int(request.GET['type'])
        y=float(year[0])
        ye=year[1]
        total = float(amount*y)
        total = total + (total*age/100)
        if age==0:
            age="18-20"
        elif age==10:
            age="21-25"
        elif age==15:
            age="26-30"
        elif age==20:
            age="31-35"
        elif age==25:
            age="36-40"
        elif age==30:
            age="41-45"
        elif age==35:
            age="46-50"
        total = int(total/typo)
        slash = "/"
        if typo==12:
                    month = "month"
        else:
                month = "months"
        if typo==4:
                typo=3
        elif typo==2:
                typo=6
        elif typo==1:
                typo=12
        elif typo==12:
                typo=1    
        if request.GET['confirm']=='check':
            return render(request,'cal_cancer.html',{'total':total, 'type' : typo , 'month':month, 'slash':slash})
        elif request.GET['confirm']=='pay':
            
            current = request.user
            caser=User_Own.objects.all()
            for ca in caser:
                if current.username==ca.user_name:
                    val=ca
                    break
            idi = val.id
            x = datetime.datetime.now()
            x=x.strftime("%x")
            detailsu = Details(name=name,age=age,amount=amount,year=ye,start_date=x,typo=typo,total=total,newid=idi)
            detailsu.save()
            # val.details.create(name=name,age=age,amount=amount,year=year,typo=typo,total=total)
            # val.details.add(detailsu)
            # val.save()
            # det = val.details.all()
            deta = Details.objects.all()
            return render(request,"profile.html",{'val':val,'detailsu':deta,'idi':idi})
    return render(request,'cal_cancer.html')

def term_calculation1(request):
    if request.method=="GET":
        name = "General Insurance"
        age = int(request.GET['age'])
        amount = int(request.GET['amount'])
        year = request.GET['year']
        year=year.split("+")
        typo = int(request.GET['type'])
        y=float(year[0])
        ye=year[1]
        total = float(amount*y)
        total = total + (total*age/100)
        if age==0:
            age="18-20"
        elif age==10:
            age="21-25"
        elif age==15:
            age="26-30"
        elif age==20:
            age="31-35"
        elif age==25:
            age="36-40"
        elif age==30:
            age="41-45"
        elif age==35:
            age="46-50"
        total = int(total/typo)
        slash = "/"
        if typo==12:
                    month = "month"
        else:
                month = "months"
        if typo==4:
                typo=3
        elif typo==2:
                typo=6
        elif typo==1:
                typo=12
        elif typo==12:
                typo=1    
              
            
        if request.GET['confirm']=='check':
            
            
            return render(request,'cal_general.html',{'total':total, 'type' : typo , 'month':month, 'slash':slash})
        elif request.GET['confirm']=='pay':
            
            current = request.user
            caser=User_Own.objects.all()
            for ca in caser:
                if current.username==ca.user_name:
                    val=ca
                    break
            idi = val.id
            x = datetime.datetime.now()
            x=x.strftime("%x")
            detailsu = Details(name=name,age=age,amount=amount,year=ye,typo=typo,start_date=x,total=total,newid=idi)
            detailsu.save()
            # val.details.create(name=name,age=age,amount=amount,year=year,typo=typo,total=total)
            # val.details.add(detailsu)
            # val.save()
            # det = val.details.all()
            deta = Details.objects.all()
            return render(request,"profile.html",{'val':val,'detailsu':deta,'idi':idi})
    return render(request,'cal_general.html')


def get_values(request):
    if request.method=="GET":
        current = request.user
        caser=User_Own.objects.all()
        for ca in caser:
            if current.username==ca.user_name:
                val=ca
                break
        idi = val.id
       
            # val.details.create(name=name,age=age,amount=amount,year=year,typo=typo,total=total)
            # val.details.add(detailsu)
            # val.save()
            # det = val.details.all()
        deta = Details.objects.all()        
        return render(request,"profile.html",{'val':val,'detailsu':deta,'idi':idi})
    return render(request,"profile.html")

def term_calculation2(request):
    if request.method=="GET":
        name = "Heart Insurance"
        age = int(request.GET['age'])
        amount = int(request.GET['amount'])
        year = request.GET['year']
        year=year.split("+")
        typo = int(request.GET['type'])
        y=float(year[0])
        ye=year[1]
        total = float(amount*y)
        total = total + (total*age/100)
        if age==0:
            age="18-20"
        elif age==10:
            age="21-25"
        elif age==15:
            age="26-30"
        elif age==20:
            age="31-35"
        elif age==25:
            age="36-40"
        elif age==30:
            age="41-45"
        elif age==35:
            age="46-50"
        total = int(total/typo)
        slash = "/"
        if typo==12:
                    month = "month"
        else:
                month = "months"
        if typo==4:
                typo=3
        elif typo==2:
                typo=6
        elif typo==1:
                typo=12
        elif typo==12:
                typo=1    
        if request.GET['confirm']=='check':
            return render(request,'cal_heart.html',{'total':total, 'type' : typo , 'month':month, 'slash':slash})
        elif request.GET['confirm']=='pay':
            current = request.user
            caser=User_Own.objects.all()
            for ca in caser:
                if current.username==ca.user_name:
                    val=ca
                    break
            idi = val.id
            x = datetime.datetime.now()
            x=x.strftime("%x")
            detailsu = Details(name=name,age=age,amount=amount,year=ye,start_date=x,typo=typo,total=total,newid=idi)
            detailsu.save()
            # val.details.create(name=name,age=age,amount=amount,year=year,typo=typo,total=total)
            # val.details.add(detailsu)
            # val.save()
            # det = val.details.all()
            deta = Details.objects.all()
            return render(request,"profile.html",{'val':val,'detailsu':deta,'idi':idi})
    return render(request,'cal_heart.html')

def pension_calculation(request):
    if request.method=="GET":
        name="Pension Plan"
        pension=int(request.GET['amount'])
        age=request.GET['year']
        age=age.split("+")
        amount=age[0]*pension
        slash = "/"
        incentive=int(pension*170000)
        ye=age[0]
        age=age[1]
        month="Month"
        if request.GET['confirm']=='check':
            return render(request,'cal_pension.html',{'total':amount,'type':incentive,'month':month,'slash':slash})
        elif request.GET['confirm']=='pay':
            current = request.user
            caser=User_Own.objects.all()
            for ca in caser:
                if current.username==ca.user_name:
                    val=ca
                    break
            idi = val.id
            x = datetime.datetime.now()
            x=x.strftime("%x")
            detailsu = Details(name=name,age=age,amount=amount,year=ye,typo=1,start_date=x,total=pension,newid=idi)
            detailsu.save()
            # val.details.create(name=name,age=age,amount=amount,year=year,typo=typo,total=total)
            # val.details.add(detailsu)
            # val.save()
            # det = val.details.all()
            deta = Details.objects.all()
            return render(request,"profile.html",{'val':val,'detailsu':deta,'idi':idi})     

    return render(request,'cal_pension.html')



def profile(request):
    current = request.user
    person = User_Own.objects.all()
    return render(request,"profile.html",{'user':current,'person':person})

def team(request):
    return render(request,"team.html")
def calculator(request):
    return render(request,"blog.html")
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
def select_form(request):
    form = request.POST['form1']
    if form == 'form1':
        return render(request,'blog.html',{'form1':form})



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                print('hi')
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                print('hi2')
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                datauser = User_Own.objects.create(first_name=first_name,last_name=last_name,user_name=username,email=email)
                datauser.save()
                print('hi3')
                print("User created")
                return redirect('login')
        else:
            print('hi4')
            messages.info(request,"Password not matched")
            return redirect('register')
        return redirect('/')
    else:
        print('h5')
        return render(request,'registration.html')
