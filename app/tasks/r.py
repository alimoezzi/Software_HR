from rq import Queue, get_current_job


def r(conn=None, a=5):
    thisjob = get_current_job(conn).id
    return list(range(a))