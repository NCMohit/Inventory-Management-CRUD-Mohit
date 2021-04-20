from django.db import models

class Entries(models.Model):
	entry_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	owner_phone_number = models.BigIntegerField()
	creation_date = models.DateTimeField(auto_now=True)
	is_working = models.BooleanField()
	image = models.ImageField(upload_to="imgs")
