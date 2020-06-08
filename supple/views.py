from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template import loader
from supple.models import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse


def signout(request):
	logout(request)

	return redirect("/")








def home(request):
    return render(request,"home.html")



def register(request):
	if request.method=="POST":
			user=request.user
			first_name=request.POST.get('first_name')
			last_name=request.POST.get('last_name')
			username=request.POST.get('username')
			email=request.POST.get('email')
			mobilenumber=request.POST.get('mobilenumber')
			password1=request.POST.get('password1')
			password2=request.POST.get('password2')
			address=request.POST.get('address')
			user=User.objects.create_user(username=first_name,password=password1,email=email)
			print(user)
			login(request,user)
			subject='Your account has been created successfully!'
			message=f'Registration Musclefactory,Thank you {user.username} for registration. Happy Shopping'
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[user.email,]
			send_mail( subject,message,email_from,recipient_list)
			if password1==password2:
				signup=Registration.objects.create(first_name=first_name,last_name=last_name, email=email,mobilenumber=mobilenumber,password1=password1,
					password2=password2,address=address)
			else:
				messages.success(request, 'Password doesnt match')
				#return redirect('/register/')
			return redirect('/store/')
			
	return render(request,'register.html')
	

def signin(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")

		user=authenticate(username=username,password=password)

		if user!=None:
			login(request,user)
			return redirect("/store/")
		# else:
		# 	return redirect("/register/")
	return render(request,"login.html")




def contactus(request):
	if request.method == "POST":
		name= request.POST["name"]
		email= request.POST["email"]
		message = request.POST["message"]
		contactus= Contact.objects.create(name=name ,email=email, message=message)
		contactus.save()
		messages.success(request, 'Your message has been sent!!')
		subject='Your message has been received!'
		message=f'thank you {{user.username}} for using Muscle Factory'
		email_from=settings.EMAIL_HOST_USER
		recipient_list=[user.email,]
		send_mail( subject,message,email_from,recipient_list)
	return render(request , 'contact.html')
	


def about(request):

	return render(request,"about.html")



def store(request):
	a=[]
	if request.method == "POST":
		user= request.user
		onwhey=  request.POST.get("onwhey",0)
		a.append(int(onwhey))
		pro=  request.POST.get("pro",0)
		a.append(int(pro))
		mbgold=  request.POST.get("mbgold",0)
		a.append(int(mbgold))
		mpwhey=  request.POST.get("mpwhey",0)
		a.append(int(mpwhey))
		rcking=  request.POST.get("rcking",0)
		a.append(int(rcking))
		mtmass=  request.POST.get("mtmass",0)
		a.append(int(mtmass))
		syntha=  request.POST.get("syntha",0)
		a.append(int(syntha))
		onmass=  request.POST.get("onmass",0)
		a.append(int(onmass))
		onbcaa=  request.POST.get("onbcaa",0)
		a.append(int(onbcaa))
		mbmulti= request.POST.get("mbmulti",0)
		a.append(int(mbmulti))
		mpcreatine= request.POST.get("mpcreatine",0)
		a.append(int(mpcreatine))
		glutamine= request.POST.get("glutamine",0)
		a.append(int(glutamine))
		asitis= request.POST.get("asitis",0)
		a.append(int(asitis))
		onshaker= request.POST.get("onshaker",0)
		a.append(int(onshaker))
		gymeq= request.POST.get("gymeq",0)
		a.append(int(gymeq))
		gymbag= request.POST.get("gymbag",0)
		a.append(int(gymbag))
		totalSum= request.POST.get("totalSum")
		all_supple=supplementsOrdered.objects.filter(user=user)
		onwhey = int(onwhey) * 7468
		pro = int(pro) * 3999
		mbgold= int(mbgold) *4799 
		mpwhey = int(mpwhey) * 4399
		rcking = int(rcking) * 5250
		mtmass = int(mtmass) * 3300
		syntha = int(syntha) * 4574
		onmass =int(onmass) * 2952
		onbcaa =int(onbcaa) * 2679
		mbmulti =int(mbmulti) * 629
		mpcreatine =int(mpcreatine) *1049 
		glutamine =int(glutamine) * 1000
		asitis =int(asitis) * 1183
		onshaker=int(onshaker) * 350
		gymeq =int(gymeq) * 7491
		gymbag =int(gymbag) * 3784
		totalSum = onwhey+pro+mbgold+mpwhey+rcking+mtmass+syntha+onmass+onbcaa+mbmulti+mpcreatine+glutamine+asitis+onshaker+gymeq+gymbag
		store = supplementsOrdered.objects.create(
			onwhey=onwhey,pro=pro,mbgold=mbgold,
			mpwhey=mpwhey,rcking=rcking,mtmass=mtmass,
			syntha=syntha, onmass=onmass, onbcaa=onbcaa, mbmulti=mbmulti,
			mpcreatine=mpcreatine, glutamine=glutamine, asitis=asitis, onshaker=onshaker,gymeq=gymeq,
			gymbag=gymbag,totalSum=totalSum)
	
		store.save()
		return render(request,'cart.html',{'a':a,'totalSum':totalSum})
	return render(request,'store.html')

def cart(request):
	obj=supplementsOrdered.objects.filter(user=request.user)
	return render(request, 'cart.html', {'obj':obj})



def order(request):
	
	return render(request, 'order.html')






def ask(request):
	if request.method == "POST":
		name=request.POST["name"]
		email=request.POST["email"]
		message=request.POST["message"]
		ask=Ask.objects.create(name=name ,email=email, message=message)
		ask.save()
		messages.success(request, 'Your message has been sent!!')
	return render(request , 'ask.html')




def shipping(request):
	if request.method=="POST":
	 user=request.user
	 firstname=request.POST.get('firstname')
	 lastname=request.POST.get('lastname')
	 username=request.POST.get('username')
	 email=request.POST.get('email')
	 mobilenumber=request.POST.get('mobilenumber')
	 address=request.POST.get('address')
	 shipping=Shipping.objects.create(username=firstname,address=address,mobilenumber=mobilenumber,email=email)
	 subject='Your order has been placed!!!'
	 message=f'your order has been placed in Musclefactory,Thank you {user.username} for shopping. your order will be delivered in 3-4 days'
	 email_from=settings.EMAIL_HOST_USER
	 recipient_list=[user.email,]
	 send_mail( subject,message,email_from,recipient_list)
	 return render(request,'order.html')
	return render(request,'shipping.html')
	

	