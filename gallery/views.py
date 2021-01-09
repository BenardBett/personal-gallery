from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # import pdb; pdb.set_trace()
    return  render(request, 'all/dashboard.html')
