WorkhouseAPI

Learning how to work with APIs on the example of an abstract place in which various professionals perform their work for clients. TechStack: Python 3.8.10, django 4.1.4, djangorestframework 3.14.0, PostgreSQL.

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

    Complete registration, authentication and authorization with API, heshing passwords and JWT access.
    Registration of new records into the schedule.
    Filtration of the schedule to simplify the search.
    Upgrade fron-end part.
