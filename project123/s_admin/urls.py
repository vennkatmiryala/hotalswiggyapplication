"""project123 URL Configuration

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
#from django.contrib import admin
from django.urls import path,include

from s_admin import views

urlpatterns = [
    #path('admin/', admin.site.urls),
path('',views.showIndex,name='main'),
    path('admin_check/',views.adminCheck,name='admin_check'),
    path('admin_menu/',views.adminMenu,name='admin_menu'),
    path('admin_logout/',views.adminLogout,name = 'admin_logout'),
    path('admin1/',views.adminOperatoin,name='admin'),

    #state
    path('state_operations/',views.stateOperations,name='state_operations'),
    path('save_state/',views.saveState,name='save_state'),
    path('updatestate/',views.updatestate,name='updatestate'),
    path('updatestated/',views.updatestated,name='updatestated'),
    path('deletestate/',views.deletestate,name='deletestate'),
    #city
    path('addcity/',views.addCity,name='addcity'),
    path('savecity/',views.savecity,name='savecity'),
    path('deletecity/',views.deletCity,name='deletecity'),
    path('updatecity/',views.updateCity,name='updatecity'),
    path('updatesave/',views.updateSave,name='updatesave'),
    #area
    path('areaoperations/',views.areaOperations,name='areaoperations'),
    path('savearea/',views.saveArea,name='savearea'),
    path('deletearea/',views.deleteArea,name='deletearea'),
    #type
    path('restrotype/',views.restroType,name='restrotype'),
    path('typesave/',views.typeSave,name='typesave'),

    # restaurant
    path('show_pending_res/', views.pending_res, name="show_pending_res"),

    path('show_approved_res/', views.show_approved_res, name="show_approved_res"),

    path('show_cancel_res/', views.show_cancel_res, name="show_cancel_res"),

    path('approve_res/', views.approve_res, name="approve_res"),
    path('cancel_res/', views.cancel_res, name="cancel_res"),

]
