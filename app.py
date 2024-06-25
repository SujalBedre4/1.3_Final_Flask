from flask import Flask, render_template, jsonify
from data import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("hello.html", jobs=jobs, company_name="Astro_Travel")


# This is for viewing the data in the jason forms:
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(load_jobs_from_db())
