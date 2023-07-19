"""loginformpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from loginformapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('main',views.mainpage,name='main'),
    path('Logout',views.Logout,name='Logout'),
    path('genrate',views.generatedata,name='genrate'),
    path('ssc',views.ssc,name='ssc'),
    path('resultdata/<d>',views.resultdata,name='resultdata'),
    path('intermidiate/<d>',views.intermidiate,name='intermidiate'),
    path('hsc',views.hsc,name='hsc'),
    path('data',views.savedata,name='data'),
    path('degreeData/<d>',views.degreeData,name='degreeData'),
    path('degree',views.degree,name='degree'),
    path('store',views.storeData,name='store'),
    path('btechData/<d>',views.btechData,name='btechData'),
    path('btech',views.btech,name='btech'),
    path('save',views.savebtech,name='save')
]
