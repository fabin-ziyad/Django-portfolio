from tkinter.tix import Form
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import MyModel,Allwork
from .forms import MyForm
 

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = RecentWork.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'home_page.html', context)
def Portfolio(request):
    full_works={
        'Allworks':Allwork.objects.all()
    }
    return render(request,'Portfolio.html',full_works)


def Contact(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
      form = MyForm()
  return render(request, 'contact.html', {'form': form})