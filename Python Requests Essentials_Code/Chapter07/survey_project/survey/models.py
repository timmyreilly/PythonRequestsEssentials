""" Survey app models """

from datetime import datetime
from survey import db


class Question(db.Model):
    """ A model for 'Question' """
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200))
    number_of_yes_votes = db.Column(db.Integer, default=0)
    number_of_no_votes = db.Column(db.Integer, default=0)
    number_of_maybe_votes = db.Column(db.Integer, default=0)

    def __init__(self,
                 question_text,
                 pub_date=None,
                 number_of_yes_votes=0,
                 number_of_no_votes=0,
                 number_of_maybe_votes=0):

        self.question_text = question_text

        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

        self.number_of_yes_votes = number_of_yes_votes
        self.number_of_maybe_votes = number_of_maybe_votes
        self.number_of_no_votes = number_of_no_votes

    def __repr__(self):
        return '<Question %d - %r>' % (self.id, self.question_text)

    def vote(self, vote_type):
        if vote_type == 'yes':
            self.number_of_yes_votes += 1
        elif vote_type == 'no':
            self.number_of_no_votes += 1
        elif vote_type == 'maybe':
            self.number_of_maybe_votes += 1
        else:
            raise Exception
