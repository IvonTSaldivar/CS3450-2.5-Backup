# Repo-2.5

## Organization, naming scheme 

coding standard for python will be pep8 follow naming conventions accordingly.
django project will follow pydanny's cookiecutters basic stucture. See his github, or book two scoops of django for more details

## Version control procedures

To edit something make a new branch `git checkout -b name-of-branch`.
Then make your changes, commit them. Push them to the remote repository on your branch
create a pull request and have one other member of the team review your changes.
when we get circleci running you should be able to see if all the unit tests pass.

Rules:
1 Don't edit master directly
2 Always have master branch in a working state without errors.

## Build instructions

To get you project up and running you will need to have docker installed.
after cloning the repo you will need to `cd Project` to change into the project folder
Then run `docker-compose build` followed by `docker-compose up`
project will be served to localhost:8000

## Project Setup and tool stack

The project is built on django wrapped up in a docker container, it is based of
pydanny's cookiecutter django build. 

Here is a list of the tools we are planning on using so far.

docker - container for django
django - python framework for webdev
flake8 - pep8 linter
pytest - unitesting program
cookiecutter - project setup for real projects, much better than django's startproject command
circleci - continuous integration and automated unitesting at every commit.
git - version control.
python3 - works with latest version of django.

## Unit testing instructions

In the project directory run the command 
`docker-compose run --rm --service-ports django /bin/sh`
to list names of containers run the command `docker ps`
then you will be inside the django shell. From here you will
be able to run django's built in testing commands (see docs) or you can run pytest (preferred)

pytest will recursively search for any and all files with test in the name and run them as unittests.
so we will have created simple django unittests in these files to aid development and monitor functionality.

CircleCi is designed to run pytest automatically upon pushing to the repo.
you will see CircleCi's output on the github Pull Request page easily.

## System testing instructions

Basically if `docker-compose-build` followed by `docker-compose up` works 
it means everything is working correctly. Docker really simplfies things so 
that we can all be developing on the same 'system'

## making an Admin User and the Django admin

enter the docker shell via the command 
`docker-compose run --rm --service-ports django /bin/sh`

run the command 
`python manage.py createsuperuser`

enter the credentials you will need to remember this
but the password is on local so security is not an issue.
then navigate to 

`localhost:8000/admin` 

login

We will be adjusting this README as needed as the project develops
