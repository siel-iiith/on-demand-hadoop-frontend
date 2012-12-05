from django.db import models
from django.db import models
from django.forms import ModelForm

class Job(models.Model):

    name = models.CharField(max_length = 100)
    jar_file = models.FileField(upload_to="documents/")
    input_path=models.CharField(max_length=100)
    output_path =models.CharField(max_length=100)
   #deadline = models.DateTimeField()

				#input_path = models.FileField(upload_to='documents/')
					#output_path = models.FileField(upload_to='documents/')
    def __unicode__(self):
	 return self.name
class Adm(models.Model):
    no_of_vms = models.CharField(max_length = 100)
    flavours = models.FileField(upload_to="documents/",blank=True)
    custom_script = models.FileField(upload_to="documents/",blank=True)

    def __unicode__(self):
	 return self.no_of_vms

class JobForm(ModelForm):
    class Meta:
	model = Job

class AdmForm(ModelForm):
    class Meta:
	model = Adm
# Create your models here.
