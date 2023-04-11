from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.urls import reverse
from django.template import loader
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.htm'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/details.htm'
    model = Question
    # context_object_name = 'latest_question_list'
    

class ResultsView(generic.DetailView):
    template_name = 'polls/results.htm'
    model = Question
    # context_object_name = 'latest_question_list'
    
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
    return HttpResponse("Hello, world. 4e8c6d5e is the polls index.")