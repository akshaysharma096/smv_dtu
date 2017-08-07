from django.contrib import admin
from .models import image_slide,our_ride,crew_sir,crew_members,partners,achievement,contact_info,about


#		THIS IS NOT WORKING WHY???


# class ExampleAdmin(admin.ModelAdmin):
#   def has_add_permission(self, request):
#     num_objects = self.model.objects.count()
#     if num_objects >= 1:
#       return False
#     else:
#       return True
@admin.register(image_slide)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['caption','image_tag']
@admin.register(our_ride)
class ProductsAdmin_ourride(admin.ModelAdmin):
    list_display = ['title','image_tag']

    
@admin.register(crew_sir)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['sir_img','title']
    def has_add_permission(self, request):
    	num_objects = self.model.objects.count()
    	if num_objects >=1:
      		return False
    	else:
      		return True

@admin.register(crew_members)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
    def has_add_permission(self, request):
      num_objects = self.model.objects.count()
      if num_objects >= 30:
          return False
      else:
          return True


@admin.register(achievement)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']

@admin.register(partners)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']
    def has_add_permission(self, request):
    	num_objects = self.model.objects.count()
    	if num_objects >=12:
      		return False
    	else:
      		return True
@admin.register(contact_info)
class ProductsAdmin(admin.ModelAdmin):

    list_display = ['number','address','email']
    def has_add_permission(self, request):
    	num_objects = self.model.objects.count()
    	if num_objects >= 1:
      		return False
    	else:
      		return True
@admin.register(about)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['info']
    def has_add_permission(self, request):
    	num_objects = self.model.objects.count()
    	if num_objects >=1:
      		return False
    	else:
      		return True

# Register your models here.
