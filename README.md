==================
E-Luminate website
==================

Google doc:
===========

https://docs.google.com/document/d/1QK7sTJmHXAQVOpIdj0TqIjNUqG7L1oAWX1wy6M9lJcA/edit#heading=h.sxeq7c7qg6hn

Project Structure:
==================


- design : Folder for design site and so on
- eluminate_web : django project site
- requirements.txt : packages used


Development
===========

Virtualenv package needed
-------------------------

Required packages:

pip http://pypi.python.org/pypi/pip
virtualenv http://pypi.python.org/pypi/virtualenv
virtualenvwrapper http://www.doughellmann.com/projects/virtualenvwrapper/

If you have them install it skip, otherwise

	sudo apt-get install python-pip

After that

	sudo pip install virtualenv
	sudo pip install virtualenvwrapper

To finish up, make sure to add this two line to your bashrc (or anything that your shell source)

export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

Creating the VirtualEnv
-----------------------

	mkvirtualenv eluminate_env

	pip install -r requirements.txt
	
Launching
---------

./manage.py syncdb
./manage.py runserver

P.S.: If you create a superuser with the first syncdb, it does not create the related account automatically,
so you need to log in in the admin and create the account there.

All the new user will create an account (done in the view).






