from django.db import models
from django.db import models
from django.forms import ModelForm

class Job(models.Model):

    name = models.CharField(max_length = 100)
    jar_file = models.FileField(upload_to="documents/")
   #deadline = models.DateTimeField()

				#input_path = models.FileField(upload_to='documents/')
					#output_path = models.FileField(upload_to='documents/')
    def __unicode__(self):
	return self.name

class JobForm(ModelForm):
    class Meta:
	model = Job

# Create your models here.
