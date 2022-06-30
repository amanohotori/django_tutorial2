from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last fivee published question."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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