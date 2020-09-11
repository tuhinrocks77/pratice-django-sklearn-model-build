from django.db import models

# Create your models here.
class Predictor(models.Model):
	loanFile = models.FileField()
	assesFile = models.FileField()