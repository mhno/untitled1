"""untitled1 URL Configuration

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
from django.conf.urls import url
from edu import views as core_views
from edu import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',views.index),
    # path('signup/',views.sign_up),
    # path('login/',views.sign_in),
    #url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^index/$', HomePageView.as_view(), name='index'),
    url(r'^login/', views.login, name='login'),
    # url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^signup/$', views.signup, name='signup'),
]


