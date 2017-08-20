from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
import requests
import time
import re
from bs4 import BeautifulSoup
from django.core.urlresolvers import resolve
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import json
from django.shortcuts import render
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.template import Context, Template
from django.template import RequestContext
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings

from django.template import RequestContext
from django.template.loader import render_to_string

from .models import image_slide,our_ride,partners,crew_members,crew_sir,achievement,contact_info,about,forum_form,solution

def first_page(request):

	context = {'slide':image_slide.objects.all(),'ride':our_ride.objects.all(),'partners':partners.objects.all(),'crew_members':crew_members.objects.all(),'sir': crew_sir.objects.all(),'achievement':achievement.objects.all(),'contact':contact_info.objects.all(),'about':about.objects.all()}
	return render(request,'content/base.html',context);

def forum(request):
	heading =[]
	question = []
	sol_save =[]
	ques_id = []
	sol_save_id = []
	num = 0;
	ansit=[]
	quest_list = forum_form.objects.all().order_by("-id");
	
	for q in quest_list:
		heading.append(q.email)
		question.append(q.question)
		ques_id.append(q.id)
		if solution.objects.filter(question = q.id).exists():
			ansit.append(solution.objects.filter(question = q.id).order_by('-id')[0])

				#NOW IN JS FILE COMPARE QUES_ID AND SOL_SAVE_ID AND IF SAME PRINT ELSE TRY SAME IN NEXT
			# num = 0

	context = {
		'ques_list':quest_list,
		'sol_save':ansit,
		'ques_id':ques_id,
		# 'ques_id':ques_id,
		}


	return render(request,'content/forum.html',context)

def add(request):
	print("ouououououoououououououou")
	email = request.GET.get('name','')
	question = request.GET.get('text','')
	print(email)
	#why not working??
	# if not question:
	# 	render(request,'content/forum.html',{'message':'please enter the query'})
	print(question)
	question_object = forum_form(email = email,question =question)
	question_object.save()

	return HttpResponse("ok")
def content(request):
	print("popopopopopopopopopopopopopopopopopop")
	heading =[]
	question = []
	sol_save =[]
	ques_id = []
	sol_save_id = []
	num = 0;
	ansit=[]
	quest_list = forum_form.objects.all().order_by("-id");
	
	for q in quest_list:
		heading.append(q.email)
		question.append(q.question)
		ques_id.append(q.id)
		if solution.objects.filter(question = q.id).exists():
			ansit.append(solution.objects.filter(question = q.id).order_by('-id')[0])

	for a in ansit:
			# if num < 2:
			sol_save.append(a.ans)
			sol_save_id.append(a.question.id)

	


				#NOW IN JS FILE COMPARE QUES_ID AND SOL_SAVE_ID AND IF SAME PRINT ELSE TRY SAME IN NEXT
			# num = 0
	print(ques_id)
	print(sol_save)
	print(sol_save_id)


	context = {
		'heading':heading,
		'question':question,
		'sol_save':sol_save,
		'sol_save_id':sol_save_id,
		'ques_id':ques_id,
		# 'ques_id':ques_id,
		}

	return JsonResponse(context,safe = False)
def add_ans(request):
	print("idiasjfs;dfhasljkdfbaslkdfbaskldfsajdfalsjkdfhaksjldfhaskjdfnaskjdfhadjlsfhasjkdfaskjdfbaskjdfbaskjbdf askjd faskjdbfakjsdbfkjasdbfadjksbfadjlsb fadjsbf adjs bfaks;d faks;d fk;asdbfajksdnfbkjaslbdnfasdnfa,.smdnfaskjdnfaskj.n")

	a = request.GET.get('solution','')
	q = request.GET.get('question','')
	print(q)
	print(a)
	quest = forum_form.objects.get(question = q)
	ques_id  = quest.id
	ans  = solution(question = quest,ans = a )
	ans.save()

		#NOW IN JS FILE COMPARE QUES_ID AND SOL_SAVE_ID AND IF SAME PRINT ELSE TRY SAME IN NEXT
			# num = 0
	print(ans.ans)
	context = {
	'ansit':ans.ans,
	'ques_id':ques_id
	}
	return JsonResponse(context,safe = False)

	return HttpResponse("ok")
def upload(request):
	return HttpResponse("ok")
def all_ans(request):
	ans = []
	ques_id = request.GET.get('ques_id','')
	ques  = forum_form.objects.filter(pk = ques_id)
	print(ques)
	all_ans = solution.objects.filter(question = ques)
	for a in all_ans:
		ans.append(a.ans)
	context = {
	'ans' : ans
	}
	print(ans);
	return JsonResponse(context,safe = False)
# Create your views here.
