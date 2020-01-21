from rq import Queue, get_current_job
from server import create_app


def r(a=5):
    thisjob = get_current_job(create_app.conn).id
    return list(range(a))