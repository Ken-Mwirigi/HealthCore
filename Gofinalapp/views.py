from django.shortcuts import render, redirect
from Gofinalapp.models import Appointment, Contact, User, ImageModel
from Gofinalapp.forms import ContactForm, ImageUploadForm
from Gofinalapp.forms import AppointmentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).exists():
            return render(request,'index.html')

        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def service(request):
    return render (request,'service-details.html ')

def starter(request):
    return render (request,'starter-page.html ')

def about(request):
    return render (request,'about.html')

def doctors(request):
    return render(request ,'doctors.html')

def services(request):
    return render(request,'services.html')



def appointment(request):
    if request.method == 'POST':
        myappointments=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
        )
        myappointments.save()
        return redirect('/appointment')

    else:
        return render(request,'appointment.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id = id)
    appoint.delete()
    return redirect('/show')

"""
#def contact(request):
    #if request.method == 'POST':
     #   mycontacts= Contact (
            #name=request.POST['name'],
            #email=request.POST['email'],
            #subject=request.POST['subject'],
            message=request.POST['message']
        )
        mycontacts.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')

"""
""""
def show(request):
    allcontacts = Contact.objects.all()
    return render(request,'show.html',{'contact':allcontacts})

def delete(request,id):
    cont = Contact.objects.get(id = id)
    cont.delete()
    return redirect('/show')
    
"""
def editt(request,id):
    editappoint =Appointment.objects.get(id = id)
    return render(request,'editt.html',{'appointment':editappoint})

def update(request,id):
    updateinfo=Appointment.objects.get(id = id)
    form=AppointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'editt.html')

def register(request):
    if request.method == 'POST':
        members = User(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render (request,'register.html')


def login(request):
    return render(request,'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

