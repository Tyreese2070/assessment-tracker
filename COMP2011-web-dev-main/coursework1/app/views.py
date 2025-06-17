from flask import render_template, flash, redirect, url_for, request
from app import app, db
from .forms import NewAssessmentForm
from .models import Assessment
from datetime import datetime

# buttons
@app.route("/incomplete/<int:id>", methods=["POST"])
def incompleteAssessment(id):
    assessment = Assessment.query.get_or_404(id)
    assessment.completion = False
    db.session.commit()
    nextPage = request.args.get("next")
    return redirect(url_for(nextPage))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def editAssessment(id):
    assessment = Assessment.query.get_or_404(id)
    form = NewAssessmentForm(obj=assessment)

    if form.validate_on_submit():
        assessment.moduleCode = form.moduleCode.data
        assessment.title = form.title.data
        assessment.description = form.description.data
        assessment.dateTime = form.dateTime.data
        db.session.commit()
        flash("Assessment updated successfully!")
        return redirect(url_for("homepage"))

    return render_template("editAssessment.html", form=form, assessment=assessment)


@app.route("/complete/<int:id>", methods=["POST"])
def completeAssessment(id):
    assessment = Assessment.query.get_or_404(id)
    assessment.completion = True
    db.session.commit()
    nextPage = request.args.get("next")
    return redirect(url_for(nextPage))

@app.route("/remove/<int:id>", methods=["POST"])
def removeAssessment(id):
    assessment = Assessment.query.get_or_404(id)
    db.session.delete(assessment)
    db.session.commit()
    nextPage = request.args.get("next")
    return redirect(url_for(nextPage))

# web pages
@app.route("/")
@app.route("/homepage")
def homepage():
    currentAssessments = Assessment.query.filter_by(completion=False).all()
    completedAssessments = Assessment.query.filter_by(completion=True).all()
    return render_template("homepage.html", current_assessments=currentAssessments, completed_assessments=completedAssessments)

@app.route("/completedAssessments")
def completedAssessments():
    completedAssessment = Assessment.query.filter_by(completion=True).all()
    return render_template("completedAssessments.html", assessments=completedAssessment)

@app.route("/currentAssessments")
def currentAssessments():
    currentAssessment = Assessment.query.filter_by(completion=False).all()
    return render_template("currentAssessments.html", assessments=currentAssessment)

@app.route("/editAssessment")
def editAssessmentPage():
    return render_template("editAssessment.html")

@app.route("/newAssessment", methods=["GET", "POST"])
def newAssessment():
    form = NewAssessmentForm()

    if form.validate_on_submit():
        moduleCode = form.moduleCode.data
        title = form.title.data
        description = form.description.data
        dateTime = form.dateTime.data

        newAssessment = Assessment(moduleCode=moduleCode, title=title, description=description, dateTime=dateTime, completion=False)

        db.session.add(newAssessment)
        db.session.commit()

        flash("New assessment added")
        return redirect(url_for('newAssessment'))

    return render_template("newAssessment.html", form=form)