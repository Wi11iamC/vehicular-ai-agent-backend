# vehicular-ai-agent-backend


This repository is a starting point for creating a REST API for data collection of the vehicular AI Agent research project. We will be using [django](https://www.djangoproject.com/), and [django-rest-framework](https://www.django-rest-framework.org/) to help develop our API and set up the models / schema for our database. We plan to use [postgreSQL](https://www.postgresql.org/) for our database. There will be data collected from various types of sensors, such as rgb camera sensor, lidar sensor, imu sensor, etc, that will be recorded from our [CARLA](https://carla.org/) (CAR Learning to Act) simulation. 

---

## Development



### Set up database and environment variables: 
Make sure that
- Environment variables are set up (create .env file and paste contents from sample.env file and edit configs) 
- The database (postgres) is up and running (Depending on your OS, setting up postgres may be different).

--- 
### Make sure to install required packages:

```sh
pip install -r requirements.txt
```

### Start Server

First, you must migrate and sync database:
```sh
python manage.py migrate
```
Next, run the server:
```sh
python manage.py runserver
```

Note that the default server is port=8000


Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000/](http://localhost:8000/)
