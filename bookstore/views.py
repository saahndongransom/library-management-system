from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from . import forms,models
from . forms import UploadFileForm
from .models import FilesUpload
from .forms import *
from .forms import BookForm
from django.forms import ModelForm
from . import forms,models
import json
from urllib.request import urlopen

# Create your views here.
def home(request):
    return render(request, "bookstore/home.html")


def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, f"Account Created for {username}")

        return redirect('login')
    else:
        form =UserRegistrationForm()
        context = {
            'form':form
        }
      
        return render(request,'bookstore/register.html', context)
    def profile(request):
        return render(request,'bookstore/profile.html')

                        
def addbook_view(request):
    
    form=forms.BookForm()
    if request.method=='POST':
     
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bookstore/bookadded.html')
    return render(request,'bookstore/addbook.html',{'form':form})
def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'bookstore/viewbook.html',{'books':books})

def addfile(request):
    if request.method =="POST":
        file2 = request.POST["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("your file was upload")
        return render(request,'bookstore/bookadded.html')
   
        return render(request,'bookstore/addfile.html')  

def dictionary(request):
    if request.method == "POST":
        form =dashboardfom(request.POST)
        text = request.POST['text']
        url ="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = request.GET.get(url)
        answer = r.Json()
        try:
            phonetic =answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition =answer[0]['definitions'][0]['definition']
            example = answer[0]['meaning'][0]['definition'][0]['example']
            synonyms =answer[0]['meaning'][0]['defintions'][0]['synonyms']
            context ={
                'form':form,
                'input':text,
                'phonetics':phonetics,
               'audio':audio,
               'definition':definition,
               'example':example,
               'synonyms':synonyms,
            }
        except:
            context = {
                'form':form,
                'input':''
            }
        return render(request,"bookstore/dictionary.html",context)
    else:

            form =dashboardfom()
    context = {'form':form}

    return render(request,'bookstore/dictionary.html',context)
