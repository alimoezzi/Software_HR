#!/usr/bin/env python

from app import *

c = create_app()
app = c.app


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

if __name__ == "__main__":
    app.run()
