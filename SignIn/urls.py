from django.urls import path
from .views import AboutFeatures, DataLibrary, IndexPageView, PreferredVendorLinks

urlpatterns = [
    path("", IndexPageView, name = 'SignIn'),
    path("about/", AboutFeatures, name = 'About'),
    path("library/", DataLibrary, name = 'Library'),
    path("vendors/", PreferredVendorLinks, name = 'Vendors')
    ]