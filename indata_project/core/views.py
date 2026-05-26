from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        contact.save()
        
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'contact.html')
