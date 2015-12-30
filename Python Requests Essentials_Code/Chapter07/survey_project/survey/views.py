"""

Task                        HTTP Method     URL

Create Survey Questions.    POST            http://[hostname:port]/questions
View list of all Questions. GET             http://[hostname:port]/questions
View a specific Question.   GET             http://[hostname:port]/questions/[question_id]
Modify a Question.          PUT             http://[hostname:port]/questions/[question_id]
Delete a Questin.           DELETE          http://[hostname:port]/questions/[question_id]
Upvote a Question.          POST            http://[hostname:port]/questions/[question_id]/vote

Other URLs

Task                        HTTP Method     URL

Home Page.                  GET             http://[hostname:port]/
New Question Form Page.     GET             http://[hostname:port]/questions/new
Voting Form Page.           GET             http://[hostname:port]/questions/[question_id]/vote
"""

from flask import render_template, request, redirect
from models import Question
from survey import app, db


@app.route('/', methods=['GET'])
def home():
    questions = Question.query.all()
    context = {'questions': questions,
               'number_of_questions': len(questions)}
    return render_template('index.html',
                           **context)


@app.route('/questions/new', methods=['GET'])
def new_questions():
    return render_template('new.html')


@app.route('/questions', methods=['POST'])
def create_questions():
    if request.form["question_text"].strip() != "":
        new_question = Question(question_text=request.form["question_text"])
        db.session.add(new_question)
        db.session.commit()
        message = "Succefully added a new poll!"
    else:
        message = "Poll question should not be an empty string!"

    context = {}
    context['questions'] = Question.query.all()
    context['message'] = message

    return render_template('index.html',
                           **context)


@app.route('/questions', methods=['GET'])
def index_questions():
    questions = Question.query.all()
    context = {'questions': questions,
               'number_of_questions': len(questions)}
    return render_template('index.html',
                           **context)


@app.route('/questions/<int:question_id>', methods=['GET'])
def show_questions(question_id):
    context = {'question': Question.query.get(question_id)}
    return render_template('show.html',
                           **context)


@app.route('/questions/<int:question_id>', methods=['PUT'])
def update_questions(question_id):
    question = Question.query.get(question_id)
    if request.form["question_text"].strip() != "":
        question.question_text = request.form["question_text"]
        db.session.add(question)
        db.session.commit()
        message = "Succefully updated a poll!"
    else:

        message = "Question cannot be empty!"

    context = {'question': question,
               'message': message}

    return render_template('show.html',
                           **context)


@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_questions(question_id):
    question = Question.query.get(question_id)
    db.session.delete(question)
    db.session.commit()
    return "This is a resource to update/modify a question basing on it's id"


@app.route('/questions/<int:question_id>/vote', methods=['GET'])
def new_vote_questions(question_id):
    question = Question.query.get(question_id)
    context = {'question': question}
    return render_template('vote.html',
                           **context)


@app.route('/questions/<int:question_id>/vote', methods=['POST'])
def create_vote_questions(question_id):
    question = Question.query.get(question_id)

    if request.form["vote"] in ["yes", "no", "maybe"]:
        question.vote(request.form["vote"])

    db.session.add(question)
    db.session.commit()
    return redirect("/questions/%d" % question.id)

