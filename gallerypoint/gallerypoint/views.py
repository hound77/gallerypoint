from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *


def show_about_page(request):
    print("aboutjj")
    return render(request, "about.html",{})

def show_home_page(request):
    cats=Category.objects.all()
    print(cats)
    images = Image.objects.all()
    data={'images':images,'cats':cats}
    return render(request,"home.html",data)

def show_category_page(request,cid):
    #print(cid)
    cats=Category.objects.all()
    category= Category.objects.get(pk=cid)
    #print(cats)
    images = Image.objects.filter(cat=category)
    data={'images':images,'cats':cats}
    return render(request,"home.html",data)

def home(request):
    return redirect('/home')

def search(request):
    print("aboutjj")
    #allimages =Image.objects.all()

    query = request.GET['query']
    allimages = Image.objects.filter(title__icontains=query)
    data = {'allimages': allimages}
    return render(request,'search.html',data)



