'''from http.client import HTTPResponse
from django.shortcuts import render''' 

from django.http import HttpResponse 

# Create your views here.

def IndexPageView(request):
    return HttpResponse ('Welcome to the sign in page!')

def AboutFeatures(request):
    return HttpResponse ('About the company: ')

def DataLibrary(request):
    return HttpResponse ('Collection of data')
    
def PreferredVendorLinks(request):
    return HttpResponse ('Follow these links below: ')
