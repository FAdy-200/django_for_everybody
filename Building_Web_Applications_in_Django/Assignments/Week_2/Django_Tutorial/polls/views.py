from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question,Choice
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.htm')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,"polls/index.htm",context)

def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
        ans = q.choice_set.all()
        ctx = {"question":q,"answers":ans}
    except Question.DoesNotExist:
        raise Http404()
    return render(request,"polls/details.htm",ctx)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def owner(request):
    return HttpResponse("Hello, world. 660110aa is the polls index.")