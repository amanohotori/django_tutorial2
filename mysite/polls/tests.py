from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        Was_published_recently() returns False for questions whose pub_date is in the future.
        Was_published_recently() は、pub_date が未来である質問に対して False を返します。
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 day.
        was_published_recently()は pub_date が1日以上古い質問に対して False を返します。
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recentlly() returns True for questions whose pub_date is within the last day.
        was_published_recentlly() は、pub_date が過去一日以内の質問に対して True を返します。
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)