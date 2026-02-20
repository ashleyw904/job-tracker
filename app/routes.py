from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import JobApplication
from app.forms import JobForm

# main app routes
main = Blueprint('main', __name__)

# dashboard (list all jobs)
@main.route("/")
def dashboard():
    jobs = JobApplication.query.all()

    applied = JobApplication.query.filter_by(status="Applied").count()
    interviewing = JobApplication.query.filter_by(status="Interviewing").count()
    offer = JobApplication.query.filter_by(status="Offer").count()
    rejected = JobApplication.query.filter_by(status="Rejected").count()

    total = JobApplication.query.count()

    return render_template(
        "dashboard.html",
        jobs=jobs,
        applied=applied,
        interviewing=interviewing,
        offer=offer,
        rejected=rejected,
        total=total
    )

# search
@main.route("/search")
def search():
    term = request.args.get("q", "")

    if not term:
        return redirect(url_for("main.dashboard"))

    results = JobApplication.query.filter(
        (JobApplication.company.ilike(f"%{term}%")) |
        (JobApplication.position.ilike(f"%{term}%"))
    ).all()

    return render_template("search_results.html", jobs=results, term=term)

# add a new job application
@main.route("/add", methods=["GET", "POST"])
def add_job():
    form = JobForm()

    if form.validate_on_submit():
        new_job = JobApplication(
            company=form.company.data,
            position=form.position.data,
            date_applied=form.date_applied.data,
            status=form.status.data,
            notes=form.notes.data
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for("main.dashboard"))

    return render_template("add_job.html", form=form)

# edit an existing job application
@main.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    form = JobForm(obj=job)

    if form.validate_on_submit():
        job.company = form.company.data
        job.position = form.position.data
        job.date_applied = form.date_applied.data
        job.status = form.status.data
        job.notes = form.notes.data

        db.session.commit()
        return redirect(url_for("main.dashboard"))

    return render_template("edit_job.html", form=form, job=job)

# delete a job 
@main.route("/delete/<int:job_id>")
def delete_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for("main.dashboard"))

# view job
@main.route("/job/<int:job_id>")
def view_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    return render_template("view_job.html", job=job)