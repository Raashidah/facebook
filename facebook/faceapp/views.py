from django.shortcuts import render
from django.http import HttpResponse
from . models import login,signup
# Create your views here.
def face(request):
    try:
        email=request.POST['email']
        user_exist=login.objects.filter(Email=email).exists()
        if user_exist==False:

            first=request.POST['fname']
            last=request.POST['lname']
            mob=request.POST['mob']
            
            password=request.POST['pwd']
            day=request.POST['day']
            print(day)
            month=request.POST['month']
            print(month)
            year=request.POST['year']
            print(year)
            birthday=day+'-'+month+'-'+year
            print(birthday)
            gend=request.POST['gender']

            user=signup(Firstname=first,Lastname=last,Mobile_Number=mob,DOB=birthday,Gender=gend)
            print(user.Firstname,user.Lastname)
            user.save()
            logobj=login(Email=email,Password=password,user_id_id=user.id)
            logobj.save()
            return render(request,'fb.html',{"message":"user saved"})
        else:
            return render(request,'fb.html',{"message":"user already exist"})
    except Exception as e:
        print(e)      
        # return render(request,'fb.html',{"message":"user registration failed"}) 
    return render(request,'fb.html')     

def log(request):
    try:
        email=request.POST['email1']
        password=request.POST['pass']
        user_log=login.objects.get(Email=email,Password=password)
        request.session['user']=user_log.id
        print(user_log.user_id_id)
        user_obj1=signup.objects.get(id=user_log.user_id_id)
        # print(user_obj1.Firstname)
        return render(request,'master.html',{"user":user_obj1})
        
    except Exception as e:
        print(e)
        return render(request,'fb.html',{"msg":"invalid username or password"})
    # return render(request,'fb.html')
def password(request):
    try:
        user_id=request.session['user']
        
        user_obj=login.objects.get(id=user_id)
        
        old=request.POST['cpass']
        
        new=request.POST['npass']
        
        if old==user_obj.Password:
            user_obj.Password=new
            user_obj.save()
            
            return render(request,'password.html',{"msg1":"password changed"}) 
    except Exception as e:
        print(e)
    return render(request,'password.html')   
   
def changeProfile(request):
    try:
        us=request.session['user']
        
        user_login=login.objects.get(id=us)
       
        users=signup.objects.get(id=user_login.user_id_id)
        
        return render(request,'profile.html',{"user1":users,"uslog":user_login}) 
    except Exception as e:
        print(e)     
    

def home(request):
    return render(request,'master.html')
def test(request):
    if request.method=='POST':
        name=request.POST['fname']
        print(name)
        return render(request,'text.html',{"user":name}) 

    return render(request,'text.html') 

       
             