import unittest
import requests

from bs4 import BeautifulSoup
from survey import db
from survey.models import Question


class TestSurveyApp(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_defaults(self):
        question = Question('Are you from India?')
        db.session.add(question)
        db.session.commit()

        self.assertEqual(question.number_of_yes_votes, 0)
        self.assertEqual(question.number_of_no_votes, 0)
        self.assertEqual(question.number_of_maybe_votes, 0)

    def test_votes(self):
        question = Question('Are you from India?')
        question.vote('yes')
        db.session.add(question)
        db.session.commit()

        self.assertEqual(question.number_of_yes_votes, 1)
        self.assertEqual(question.number_of_no_votes, 0)
        self.assertEqual(question.number_of_maybe_votes, 0)

    def test_title(self):
        title = "Welcome to Survey Application"
        response = requests.get("http://127.0.0.1:5000/")
        soup = BeautifulSoup(response.text)
        self.assertEqual(soup.title.get_text(),
                         title)
