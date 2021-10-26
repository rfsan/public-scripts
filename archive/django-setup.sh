#!/bin/bash

# PARAMETERS
project_name="$1"
apps="${@:2}"

# EXECUTION
mkdir $project_name && cd $project_name
virtualenv venv && source venv/bin/activate
pip install django
django-admin startproject $project_name .
git init
# Creation of .gitignore file
cat > .gitignore <<- EOM
venv/
db.sqlite3
EOM
for app in $apps
do
    python manage.py startapp $app
done