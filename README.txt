WorkhouseAPI

Learning how to work with APIs on the example of an abstract place in which various professionals perform their work for clients. TechStack: Python 3.8.10, django 4.1.4, djangorestframework 3.14.0, PostgreSQL (psycopg2).

The main possibilities:

    Creating of new administrators and managers
    API for administrators, which allows you to record a person for free time to a specific specialist.
    API for managers, allowing you to create specialists, places and working hours for them.
    API for users which allows you to get a list of specialists, the time of appointment of a specialist for a specific day.
    The front-end part to visualize processes

Done things:

    Simple registration for Administrator/Manager of Workhouse
    API routes to watch/create workers, type of work, location, appointments and schedule.
    Simple front-end part.

TODO things:

    Registration of new records into the schedule. (done)
    Filtration of the schedule to simplify the search.
    Upgrade fron-end part.


UPDATE 22.12.22
Simplified models and serializers and views code in user_api
Added URL router to simplify paths in url.py

UPDATE 04.01.23
Simplified API rotes in urls.py
Added coments to some files

UPDATE 15.01.23
Added permissions
Added token authentication
Added part of appointment data verification