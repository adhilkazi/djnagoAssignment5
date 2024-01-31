from django.shortcuts import render,redirect
from.models import vfn
from.form import AddForm
from django.contrib import messages



# Create your views here.

#inserte view
def insert(request): 
    if request.method=="POST":
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       password=request.POST.get('password')
       conform_password=request.POST.get('conform_password')
       gender=request.POST.get('gender')
       vfn(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password,conform_password=conform_password,gender=gender).save()
       return redirect("login")
    return render(request,"singnup.html")

#view html page in another html
def views(request):
    cr=vfn.objects.all()
    return render(request,"views.html",{'cm':cr}) #views

#delete 
def delete(request,pk): 
    cr=vfn.objects.get(id=pk)
    cr.delete()
    return redirect ('views')

#detialsview
def detials_view(request,pk):
    cr=vfn.objects.get(id=pk)
    return render(request,"detials_view.html",{'cm':cr})

#update
def update(request,pk):     
    cr=vfn.objects.get(id=pk)
    form=AddForm(instance=cr)
    if request.method=="POST":
        form=AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("views")
    return render(request,"update.html",{'form':form})  

#login page show
def login(request):
    return render(request,"login.html")  

# click to login
def welcome(request):
    id=request.session['id']
    firstname=request.session['firstname']
    email=request.session['email']
    return render(request,"welcom.html",{'id':id,'firstname':firstname,'email':email})

def userlog(request):
    if request.method=="POST":
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cr=vfn.objects.filter(phone=phone,password=password)
        if cr:
            user_details=vfn.objects.get(phone=phone,password=password)
            id=user_details.id
            phone=user_details.phone
            email=user_details.email
            request.session['id']=id
            request.session['phone']=phone
            request.session['email']=email
            return redirect('welcome')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
         
    else:
        return render(request,'views.html')    
