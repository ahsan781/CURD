from django import forms
from .models import District , SubDistrict , Neighbor , SubNeighbor


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = ('name',)

class SubDistrictForm(forms.ModelForm):
    
    class Meta:
        model = SubDistrict
        fields = ('SubDistrictname','District',)
    
    def __init__(self, *args, **kwargs):
        super(SubDistrictForm,self).__init__(*args, **kwargs)
        self.fields['District'].empty_label = "Select"
class NeighborForm(forms.ModelForm):
    
    class Meta:
        model = Neighbor
        fields = ('subDistrict','Neighborname',)

    def __init__(self, *args, **kwargs):
        super(NeighborForm,self).__init__(*args, **kwargs)
        self.fields['subDistrict'].empty_label = "Select"
class SubNeigborForm(forms.ModelForm):
    
    class Meta:
        model = SubNeighbor
        fields = ('Neigbour','SubNeighborname',)

    def __init__(self, *args, **kwargs):
        super(SubNeigborForm,self).__init__(*args, **kwargs)
        self.fields['Neigbour'].empty_label = "Select"