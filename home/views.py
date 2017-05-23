from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from polls.models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
 
def home(request):
    latest_question_list = Question.objects.order_by('-created')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request, 'home/home.html', context)



