from django.shortcuts import render
from .models import image_slide,our_ride,partners,crew_members,crew_sir,achievement,contact_info,about

def first_page(request):

	context = {'slide':image_slide.objects.all(),'ride':our_ride.objects.all(),'partners':partners.objects.all(),'crew_members':crew_members.objects.all(),'sir': crew_sir.objects.all(),'achievement':achievement.objects.all(),'contact':contact_info.objects.all(),'about':about.objects.all()}
	return render(request,'content/base.html',context);


# Create your views here.
