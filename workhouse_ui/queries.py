"""
This file is created only for learning SQL and practice in SQL queries.
"""


from django.db import connection


def get_workers(new_worker=None):
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT * FROM worker_api_worker """)
        row = cursor.fetchall()
        for names in row:
            if new_worker in names:
                return 'This worker is already exists!'
    return row

print(get_workers())