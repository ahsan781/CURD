from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('districtform/', views.DistrictFrom, name='dform'),
    path('<int:id>/',views.DistrictFrom, name='updateform'),
    path('ddelete/<int:id>', views.ddelete ,name='ddelete'),
    path('subdistrictform/', views.subDistrictFrom, name='sdform'),
    path('subdistricthome/', views.subdistricthome, name='sdhome'),
    path('subdistrictform/<int:id>/',views.subDistrictFrom, name='sdupdateform'),
    path('sddelete/<int:id>', views.sddelete ,name='sddelete'),
    path('neighborform/', views.neighborFrom,  name='nform'),
    path('neighborhome/', views.neighborhome, name='nhome'),
    path('neighborform/<int:id>/',views.neighborFrom, name='nupdateform'),
    path('ndelete/<int:id>', views.ndelete ,name='ndelete'),
    path('subneighborform/', views.subneighborFrom,  name='snform'),
    path('subneighborhome/', views.subneighborhome, name='snhome'),
    path('subneighborform/<int:id>/',views.subneighborFrom, name='snupdateform'),
    path('sndelete/<int:id>', views.sndelete ,name='sndelete'),
    
    # path('dedit/<int:id>', views.dedit, name='dedit'),
    # path('subdistrict', views.subdistrcit, name='subdistrcit')

]