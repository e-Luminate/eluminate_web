==================
E-Luminate website
==================

# Google doc:


https://docs.google.com/document/d/1QK7sTJmHXAQVOpIdj0TqIjNUqG7L1oAWX1wy6M9lJcA/edit#heading=h.sxeq7c7qg6hn

# Project Structure:

- design : Folder for design site and so on
- eluminate_web : django project site
- requirements.txt : packages used


# Development

The following instuctions asume a Debian/Ubuntu linux environment

## Virtualenv package needed

- pip http://pypi.python.org/pypi/pip
- virtualenv http://pypi.python.org/pypi/virtualenv
- virtualenvwrapper http://www.doughellmann.com/projects/virtualenvwrapper/

## Other stuff also needed

- node-less

## How to install them:

If you have them install it skip, otherwise

	sudo apt-get install python-pip node-less
	
(Note: the version of lessc provided by node-less needs to be 1.3 or better. Check using "lessc -v". Ubuntu releases before 12.10 do not have a sufficiently up-to-date version.) 

After that

	sudo pip install virtualenv
	sudo pip install virtualenvwrapper

To finish up, make sure to add this two line to your bashrc (or anything that your shell source)

	export WORKON_HOME=~/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh

# Installing Postgresql database 

We will use postgresql as our database backend, therefore we need to install it

For Ubuntu

More info here, https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#creating-a-spatial-database-template-for-postgis,
however we this is the way to do it on an Ubuntu

For 10.10:

    sudo apt-get install binutils gdal-bin postgresql-8.4-postgis \
         postgresql-server-dev-8.4 python-dev
         

For 12.04:

    sudo apt-get install binutils gdal-bin postgresql-9.1-postgis \
         postgresql-server-dev-9.1 python-dev
         
Now we have to create the template to include spatial information on the database.
If you want to know everything, just read here 
https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#creating-a-spatial-database-template-for-postgis
otherwise there is ascript that can do it for you

    wget https://docs.djangoproject.com/en/dev/_downloads/create_template_postgis-debian.sh
    sudo -u postgres sh create_template_postgis-debian.sh

# Create the development user for DB on Ubuntu


Ok, now we can create the user, the database and make sure we can connect
  
    sudo -u postgres createuser e_luminate_user

answer "y" to the question about superuser if you want (doesn't matter)

    sudo -u postgres createdb -O e_luminate_user -T template_postgis e_luminate_db
    sudo -u postgres psql -c "alter user e_luminate_user with password 'e_luminate_password';"


We need be able to connect, even if our user is the one running the process..
This is for local development, so no worries (on a MAC I have no idea were is it!)


Change the line in the file /etc/postgresql/9.1/main/pg_hba.conf

from

    local   all             postgres                                peer

to

    local   all         all                               md5


and restart postgresql

    sudo /etc/init.d/postgresql restart

More info here http://www.depesz.com/index.php/2007/10/04/ident/

# get the repository

cd to the directory in which you want the Django directory to be created

	git clone https://github.com/e-Luminate/eluminate_web
	cd eluminate_web

# Creating the VirtualEnv and installing the required packages

	mkvirtualenv eluminate_env
	pip install -r requirements.txt



# Syncing the db

	./manage.py syncdb
	
If you're asked whether you want to create a superuser, answer "yes"

You will also have to migrate the database -- the app uses south, but you have to do the separate apps in the right order:

    ./manage.py migrate participant
    ./manage.py migrate events
    ./manage.py migrate maps

# Launching with honcho

Make sure you have lessc compiler installed.
Read more here: https://github.com/e-Luminate/eluminate_web/blob/master/scripts/README.md

If you've reset your machine, you will need to reactivate the virtualenv:

        workon eluminate_env

or

        source ~/.virtualenvs/eluminate_env/bin/activate
        
After that, you can start the less compiler and the development webserver (on 127.0.0.1:8000):

	honcho -f Procfile.dev start

