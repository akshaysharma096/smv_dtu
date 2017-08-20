from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class image_slide(models.Model):
	slide_image = models.ImageField(blank = False);
	caption = models.CharField(max_length = 1024,default = " " ,blank = True);

	def image_tag(self):
   		return mark_safe('<img src="%s" width="150" height="150" />' % (self.slide_image.url))
	
	def get_model_fields(model):
   		return model._meta.fields

class achievement(models.Model):
	achievments_image = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " ",blank = True);
	content = models.TextField(max_length = 1024,default = " ",blank = True);
	date = models.CharField(max_length = 1024,default = " ",blank = True);
	def image_tag(self):
   		return mark_safe('<img src="%s" width="150" height="150" />' % (self.achievments_image.url))
	def get_model_fields(model):
   		return model._meta.fields

class our_ride(models.Model):
	our_ride_image = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " ",blank = True);
	def image_tag(self):
   		return mark_safe('<img src="%s" width="150" height="150" />' % (self.our_ride_image.url))


class crew_sir(models.Model):
	sir_img = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_1 = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_2 = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_3 = models.CharField(max_length = 1024,default = " " ,blank = True);
	def image_tag(self):
   		return mark_safe('<img src="%s" width="150" height="150" />' % (self.sir_img.url))
	def get_model_fields(model):
   		return model._meta.fields

class crew_members(models.Model):
	title = models.CharField(max_length = 1024,default = " " ,blank = True);
class partners(models.Model):
	logo = models.ImageField(blank = False);
	name = models.CharField(max_length = 1024,default = " " ,blank = True);
	links = models.CharField(max_length = 1024,default = " " ,blank = True);
	def image_tag(self):
   		return mark_safe('<img src="%s" width="150" height="150" />' % (self.logo.url))

	def get_model_fields(model):
   		return model._meta.fields

class contact_info(models.Model):
	number = models.CharField(max_length = 1024,default = " " ,blank = True);
	address = models.CharField(max_length = 1024,default = " " ,blank = True);
	email = models.CharField(max_length = 1024,default = " " ,blank = True);
class about(models.Model):
	info =  models.TextField(max_length = 10024,default = " ",blank = True);


	def get_model_fields(model):
   		return model._meta.fields

class forum_form(models.Model):
	email =  models.CharField(max_length = 1024,default = " " ,blank = True);
	question = models.TextField(max_length = 1024,default =  " ",blank = False);
	answers = models.TextField(max_length = 1024,default = " ",blank = False);


	def get_model_fields(model):
   		return model._meta.fields


class solution(models.Model):
	question = models.ForeignKey(forum_form,on_delete=models.CASCADE)
	ans = models.TextField(max_length = 1024,default = " ",blank = False);
	created = models.DateTimeField(auto_now_add = True,blank = False,null =True)



	def get_model_fields(model):
   		return model._meta.fields