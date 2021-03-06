"""Django_OAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from OASapp import views

urlpatterns = {
    path('', views.index),
    path('ajax/', views.ajax_get),
    path('admin/', admin.site.urls),
    path('ajax_words/', views.ajax_words),
    path('ajax_del_word/', views.ajax_del_word),
    path('get_top_five_words/', views.get_top_five_words),
}
