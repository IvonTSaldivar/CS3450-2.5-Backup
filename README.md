# Repo-2.5

To get you project up and running you will need to have docker installed.

after cloning the repo you will need to `cd Project' to change into the project folder

Then run `docker-compose build' followed by `docker-compose up'

project will be served to localhost:8000

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

## Additional notes

We will be adjusting this README as needed as the project develops

