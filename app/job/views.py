import json

from flask import Blueprint, render_template, jsonify, request, make_response
from rq import Queue
from rq.job import Job
from app import *
from app import func
from Models import JobModel

job = Blueprint('job', __name__)


@job.route('/add_job', methods=['POST', 'GET'])
def add_job():
    if request.method == 'GET':
        return render_template('job/job_add.html', func=func.keys())
    elif request.method == 'POST':
        values = request.json
        p = values['password']
        d = values['description']
        f = values['func']
        if p and d and f:
            if p == '22m24m':
                job: Job = create_app.q.enqueue_call(
                    func=func[f], args=(), result_ttl=10800
                )
                JobModel(str(job.get_id),"",d)
                s = json.dumps({'Result': 'Success'})
                return make_response(s, 200,
                                     {'Content-Type': 'application/json'})
    s = json.dumps({'error': 'Failed to get parameters'})
    return make_response(s, 200,
                         {'Content-Type': 'application/json'})


@job.route('/job_res')
def status_job():
    j = JobModel.query.all()
    l = [{
        'job_id':j.jid,
        'date':j.created,
        'des':j.description,
        'status':' '.join(
            [
                Job.fetch(j.jid, connection=create_app.conn).is_started,
                Job.fetch(j.jid, connection=create_app.conn).is_finished,
                Job.fetch(j.jid, connection=create_app.conn).is_failed,
                Job.fetch(j.jid, connection=create_app.conn).is_queued,
                Job.fetch(j.jid, connection=create_app.conn).is_deferred,
            ]
        )
    } for i in j]
    return render_template('job/job_res.html')


@job.route('/job_res/<job_key>')
def status_job(job_key):
    job = Job.fetch(job_key, connection=create_app.conn)
    print(job.get_id, job.is_finished, job.is_started)
    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202


def r(a : int):
    return list(range(a))
