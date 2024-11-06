from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.utils import timezone
from .models import Question


def index(request):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Verifica se a questão é no futuro
    if question.pub_date > timezone.now():
        raise Http404("Esta pergunta ainda não está disponível.")

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
