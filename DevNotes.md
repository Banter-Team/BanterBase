## Using the virtual enviroment:
from the base directory use 'source venv\Scritps\activate' and you should see (venv) before your command input. This means you are in. If you add any fun things to the project that require any outside python libraries or css resources, make sure you are downloading them to the virtual enviroment and not your local computer. This will ensure that everything works on everybodies computer.

## Various "managing" Commands - use form the project directory:
1. 'python manage.py runserver' - runs the server on your local host. you can add a port and ip after this but thats kinda useless unless you want two running at once.
2. 'python manage.py makemigrations' - saves the changes from any registeres models.py files
3. 'python manage.py migrate'  - takes any saved changes from the above commands and applies is to the sql file. If there is already data in the file it will most likely ask to add defaults to any new columns you made.

## Various admin commands - use form anywhere in the virtual enviroment:
1. 'django-admin dbshell' - this is a nifty little command that gives you a shell that is integrated with the django enviroment. This is really nice for manually interacting with the database. You can directly add/remove items in the database. This is really nice for making test users or really testing anything in the db.
2. 'django-admin flush' - this just deletes the whole data base. I probably wouldnt use this. It will delete super and admin users which is really annoying to fix
3. 'django-admin startapp appname' - Starts an app. Immediatly go and add the app name to the list of registered apps in the settings or it won't even register that it is there when you run a server.
4. 'django-admin createsuperuser' - you will then be prompted for an email and username. You can make as many of these as we want, but it would probably be nice to only have a few floating around to keep track of. This user can access the admin page which is super helpful. See below

## Admin Page:
To get to the admin page go to 'localhost:8000/admin'. To get in you have to log in with a superuser. From here you get a really nice display of the data in the database. Super helpful. Keep in mind you have to register each model individually in that apps admin.py file before you can see it on the admin page
