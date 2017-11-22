from django.db import models

# Create your models here.
class Application(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	position = models.CharField(max_length=100)
	year_of_exp = models.IntegerField()
	message = models.TextField()
	app_status = models.CharField(max_length=10)
	created_on = models.DateField()

	# class Meta:
	# 	db_table = 'application'