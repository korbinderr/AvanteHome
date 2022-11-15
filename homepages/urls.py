from django.urls import path
from .views import indexPageView
from .views import signInPageView

urlpatterns = [
    path("", indexPageView, name ="index"),
    path("signin/", signInPageView, name = "SignIn")
]