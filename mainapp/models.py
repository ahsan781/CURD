from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubDistrict(models.Model):
    SubDistrictname = models.CharField(max_length=100)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self. SubDistrictname
class Neighbor(models.Model):
  id = models.AutoField(primary_key=True)
  subDistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
  Neighborname = models.CharField(max_length=200)
  def __str__(self):
        return self.Neighborname
class SubNeighbor(models.Model):
  id = models.AutoField(primary_key=True)
  Neigbour = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
  SubNeighborname = models.CharField(max_length=200)
  def __str__(self):
        return self.SubNeighborname