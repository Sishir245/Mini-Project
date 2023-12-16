from django.contrib.auth import authenticate, login # type: ignore
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from voltaire.models import Register, Appointment, Contact
from miniproject import settings
from django.core.mail import send_mail
from datetime import datetime




# Create your views here.
def home(request):
 return render(request,'home.html')

def aboutus(request):
 return render(request,'aboutus.html')

def appointment(request):

   if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      num = request.POST['num']
      comment = request.POST['comment']
      date = request.POST['date']
      print(date)
      print(date.__class__)
      time = request.POST['time']
      
      date_obj = datetime.strptime(date, '%Y-%m-%d').date()
      if Appointment.objects.filter(date=date_obj).exists():
         return render(request,'appointment.html', {'error': True})
      myuser = Appointment(name=name, email=email, num=num, comment=comment, date=date, time=time)
      myuser.save()      

#Welcome Email
      subject = "Your Appointment has been confirmed!!! "
      message ="Hello" + myuser.name + "!! \n" + "Welcome to Voltaire:Overseas Education Consultancy \nThank you for making an appointment with us. \nYou will be appointed to one of our most trusted counsellors.\n\nThanking You\n Voltaire IT Team."
      from_email = settings.EMAIL_HOST_USER
      to_list = [myuser.email]
      send_mail(subject,message, from_email, to_list, fail_silently=False)

      return redirect('home')


   return render(request,'appointment.html')

def contact(request):
 
 if request.method == 'POST':
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      number = request.POST['number']
      email = request.POST['email']
      comment = request.POST['comment']

      myuser = Contact(firstname=firstname, lastname=lastname, number=number, email=email, comment=comment)
      myuser.save()
      

      #Welcome Email
      subject = "Contact Voltaire for more Information !!! "
      message ="Hello" + myuser.firstname + "!! \n" + "Welcome to Voltaire:Overseas Education Consultancy. \nOur Team will contact you on your registered Email ID within 3-5 business days.\n\nThanking You.\nVoltaire IT Team."
      from_email = settings.EMAIL_HOST_USER
      to_list = [myuser.email]
      send_mail(subject,message, from_email, to_list, fail_silently=False)


      return redirect('home')


 return render(request,'contact.html')

def destination(request):
 return render(request,'destination.html')


def process(request):
 return render(request,'process.html')


def retry(request):
 return render(request,'retry.html')

def scholarship(request):
 return render(request,'scholarship.html')

def services(request):
 return render(request,'services.html')

def test(request):
 return render(request,'test.html')

def universities(request):
 return render(request,'universities.html')



def register(request):
 
   if request.method == 'POST':
      fname = request.POST['fname']
      lname = request.POST['lname']
      username = request.POST['username']
      email = request.POST['email']
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']

      if Register.objects.filter(username=username):
         return render(request,'register.html', {'user_error': '* Please change your Username.'})
 
      if Register.objects.filter(email=email):
            return render(request,'register.html', {'email_error': '* Email is already in use.'})

      if pass1 != pass2:
        return render(request,'register.html', {'pass_error': '* Your Password do not match.'})

      myuser = Register(first_name=fname, last_name=lname, username=username, email=email,password=pass1)
      myuser.save()



      #Welcome Email
      subject = "Your Email has been Registered!!! "
      message ="Hello " + myuser.first_name + "!! \n" + "Welcome to Voltaire:Overseas Education Consultancy. Thank you for visiting us. \n\nThanking You. \nVoltaire IT Team."
      from_email = settings.EMAIL_HOST_USER
      to_list = [myuser.email]
      send_mail(subject,message, from_email, to_list, fail_silently=False)

      return redirect('login')

   return render(request,'register.html')



def login(request):
 
   if request.method == 'POST':
      email= request.POST['email']
      pass1= request.POST['pass1']

      myuser = Register.objects.filter(email=email, password=pass1)
      if len(myuser) != 0:
         #Welcome Email
         subject = "Your Log In has been Successful. "
         message ="Hello " + myuser[0].first_name + "!! \n" + "Welcome to Voltaire:Overseas Education Consultancy. \nYou are successfully logged In. \n\nThanking You. \n Voltaire IT Team."
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser[0].email]
         send_mail(subject,message, from_email, to_list, fail_silently=False)
         return redirect('home')
      else:
        return render(request,'login.html', {'error_message': 'Invaid Email ID or Password'})

   return render(request,'login.html')
