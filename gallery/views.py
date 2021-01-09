from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Category,Image,Location
# Create your views here.

def home(request):
    # import pdb; pdb.set_trace()
    return  render(request, 'all/dashboard.html')

def about(request):
    return  render(request, 'all/about.html')  

def images(request):
    images= Image.objects.all()
    categories= Category.objects.all()
    location= Location.objects.all()
    return render(request, 'all/images.html',locals())