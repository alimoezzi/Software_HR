#!/usr/bin/env python

from app import *


c = create_app()
app = c.app
manager = create_app.manager


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))

# Add users for the example
with app.app_context():
    try:
        u = User.query.filter_by(username='admin').first()
        if not u:
            u = User(
                username='admin',
                password='admin',
                email='test@example.com',
                roles='admin',
                is_active=True
            )
            db.session.add(u)
            db.session.commit()
    except Exception as e:
        print(e)


@manager.command
def run_worker():
    """Initializes a slim rq task queue."""
    listen = ['default']
    conn = create_app.conn
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work(logging_level='DEBUG')

if __name__ == "__main__":
    manager.run()
