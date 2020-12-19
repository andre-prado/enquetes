from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, quest_id):
    question = get_object_or_404(Question, pk=quest_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, quest_id):
    response = f"You're looking at the results of question {quest_id}"
    return HttpResponse(response)


def vote(request, quest_id):
    return HttpResponse(f"You're voting on question {quest_id}")
