from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, quest_id):
    return HttpResponse(f"You're looking at question {quest_id}")


def results(request, quest_id):
    response = f"You're looking at the results of question {quest_id}"
    return HttpResponse(response)


def vote(request, quest_id):
    return HttpResponse(f"You're voting on question {quest_id}")
