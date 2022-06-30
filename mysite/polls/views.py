from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
#    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question': question})
    
#    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # POST データに choice がなければ、Question の detail 質問投票フォームを再表示する
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_massage': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

         # POST データを正常に処理した後は、常に HttpResponseRedirect を返します。これにより、ユーザが戻るボタンを押した場合に、データが二重に投稿されることを防ぐことができます。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))