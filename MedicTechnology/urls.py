"""MedicTechnology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from techmed.views import FirstView, NewTechnology
from AOITM.views import LandingPage, Register, ValidateAccount, Login, Logout, NewTechnology

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main-page', FirstView.as_view(), name='main-page'),
    # path('new-technology', NewTechnology.as_view(), name='new-technology'),
    path('', LandingPage.as_view(), name='landing-page'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('validate-account/<slug:token_value>', ValidateAccount.as_view(), name='validate-account'),
    path('add-technology', NewTechnology.as_view(), name='add-technology')
]
