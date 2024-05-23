from django.db import models

# Create your models here.
class index_view(models.Model):
    zroLocation=models.CharField(max_length=122)
    ApplyFor=models.CharField(max_length=122)
    connectionType=models.CharField(max_length=122)
    firstName=models.CharField(max_length=122)
    middleName=models.CharField(max_length=122)
    lastName=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    Mobile=models.CharField(max_length=122)
    Addr=models.CharField(max_length=122)
    Land=models.CharField(max_length=122)
    pinAdd=models.CharField(max_length=122)
    locaAdd=models.CharField(max_length=122)
    subLoc=models.CharField(max_length=122)
    assem=models.CharField(max_length=122)
    vilAdd=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.firstName