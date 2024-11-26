from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import *

# Create your views here.
def index(request):
    portfolio=Portfolio.objects.all()
    about=About.objects.all()
    skill=Skill.objects.all()
    resume=Resume.objects.all()
    summary=Summary.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    project=Project.objects.all()
    service=Service.objects.all()
    contactinfo=ContactInfo.objects.all()


    context={
        'portfolio':portfolio,
        'about':about,
        'skill':skill,
        'resume':resume,
        'summary':summary,
        'education':education,
        'experience':experience,
        'project':project,
        'service':service,
        'contactinfo':contactinfo,
    

    }

    return render(request,'user/index.html',context)




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Adjust 'contact' to your contact page's URL name
    else:
        form = ContactForm()
    return render(request, 'user/contact.html', {'form': form})
