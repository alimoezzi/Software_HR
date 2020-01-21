from flask import Blueprint, render_template, jsonify
from rq import Queue
from rq.job import Job
from app import *

main = Blueprint('main', __name__)


@main.route('/')
@cross_origin()
def index():
    job : Job = create_app.q.enqueue_call(
        func=r, args=(5,), result_ttl=5000
    )
    #render_template('main/index.html')
    return job.get_id()


@main.route('/status')
def status():
    return jsonify({'message': 'ok'}), 200\



@main.route('/status/<job_key>')
def status_job(job_key):
    job = Job.fetch(job_key, connection=create_app.conn)
    print(job.get_id, job.is_finished, job.is_started)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202


def r(a : int):
    return list(range(a))
