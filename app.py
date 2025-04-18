from flask import Flask, jsonify, render_template, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Job not found", 404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)

  return render_template('application_submission.html', application=data, job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)