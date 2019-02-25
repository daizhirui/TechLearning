from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from .models import Question, Choice

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #        'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    # use render() instead
    
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    
    # use get_object_or_404 instead
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    
    #selected_choice.votes += 1
    # use F() to avoid race condition
    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    # Always return an HttpResponseRedirect after successfully dealing with POST data.
    # This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    #return HttpResponse("You're voting on question %s." % question_id)
"""

"""
Use generic view

attributes:
    - template_name: automatically generated template file path, change it for customization
    - context_object_name: automatically generated context variable for the template, change it for customization
    - model: the model class for the view
"""

from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # automatical result: question_list

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5] 
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    
    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

