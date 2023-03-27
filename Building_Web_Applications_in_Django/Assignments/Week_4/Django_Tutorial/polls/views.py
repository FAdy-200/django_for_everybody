from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.htm', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.htm', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def owner(request):
    return HttpResponse("Hello, world. 660110aa is the polls index.")