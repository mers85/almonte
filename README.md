# Almonte

Almonte is a Django REST framework API.
The main functionalities are registration and management of Brotherhoods.

## Local Setup / Installation

```bash
$ git clone  https://github.com/mers85/almonte.git
$ cd almonte
$ pipenv install
$ pipenv shell
(almonte) $ python manage.py createsuperuser # you'll need this user to access to administration
(almonte) $ ./manage.py runserver
´´´
Navigate to the list view at http://127.0.0.1:8000/brotherhoods/ and detail view at http://127.0.0.1:8000/brotherhoods/1/.

![ListView](https://raw.githubusercontent.com/mers85/almonte/master/brotherhoods.png)

![DetailView](https://raw.githubusercontent.com/mers85/almonte/master/brotherhoods_show.png)
