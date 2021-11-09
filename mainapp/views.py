from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from mainapp.models import District, SubDistrict,Neighbor, SubNeighbor
from .forms import DistrictForm ,SubDistrictForm, NeighborForm, SubNeigborForm 

# Create your views here.
def home(request):
     district = District.objects.all()
     context = {'district':district}
     return render(request, "home.html" , context)
def DistrictFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = DistrictForm()
            else:
             district = District.objects.get(pk=id)
             form = DistrictForm(instance=district)
            return render(request, "district_form.html", {'form': form})
      else:
           
           if id == 0:
                form = DistrictForm(request.POST)
           else:
              district = District.objects.get(pk=id)
              form =  DistrictForm(request.POST,instance= district)
           if form.is_valid():
             form.save()
             return redirect('/')

def ddelete(request,id):
    employee = District.objects.get(pk=id)
    employee.delete()
    return redirect('/')
def subDistrictFrom(request, id=0):
        if request.method == "GET":
            if id == 0:
                  form = SubDistrictForm()
            else:
             subdistrict = SubDistrict.objects.get(pk=id)
             form = SubDistrictForm(instance = subdistrict)
            return render(request, "subdistrictform.html", {'form': form})
        else:
           
           if id == 0:
                form = SubDistrictForm(request.POST)
           else:
              subdistrict = SubDistrict.objects.get(pk=id)
              form =  SubDistrictForm(request.POST,instance = subdistrict)
           if form.is_valid():
              form.save()
              return redirect('/subdistricthome')
def subdistricthome(request):
     Subdistrict = SubDistrict.objects.all()
     context = {'subdistrict':Subdistrict}
     return render(request, "subdistricthome.html" , context)
def sddelete(request,id):
    subdistrict = SubDistrict.objects.get(pk=id)
    subdistrict.delete()
    return redirect('/subdistricthome')
def neighborhome(request):
     neighbor = Neighbor.objects.all()
     context = {'neighbor':neighbor}
     return render(request, "neighborhome.html" , context)
def neighborFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = NeighborForm()
            else:
             neighbor = Neighbor.objects.get(pk=id)
             form = NeighborForm(instance=neighbor)
            return render(request, "neighborform.html", {'form': form})
      else:
           
           if id == 0:
                form = NeighborForm(request.POST)
           else:
              district = Neighbor.objects.get(pk=id)
              form =  NeighborForm(request.POST,instance= district)
           if form.is_valid():
             form.save()
             return redirect('/neighborhome')

def ndelete(request,id):
    employee = Neighbor.objects.get(pk=id)
    employee.delete()
    return redirect('/neighborhome')
def subneighborhome(request):
     sneighbor = SubNeighbor.objects.all()
     context = {'sneighbor':sneighbor}
     return render(request, "subneighborhome.html" , context)
def subneighborFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = SubNeigborForm()
            else:
             sneighbor = SubNeighbor.objects.get(pk=id)
             form = SubNeigborForm(instance=sneighbor)
            return render(request, "subneighborform.html", {'form': form})
      else:
           
           if id == 0:
                form = SubNeigborForm(request.POST)
           else:
              sneighbor = SubNeighbor.objects.get(pk=id)
              form =  SubNeigborForm(request.POST,instance= sneighbor)
           if form.is_valid():
             form.save()
             return redirect('/subneighborhome')

def sndelete(request,id):
    employee = SubNeighbor.objects.get(pk=id)
    employee.delete()
    return redirect('/subneighborhome')