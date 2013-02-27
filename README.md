# The Gauntlet

#### [Flask](http://flask.pocoo.org/) vs [Django](https://www.djangoproject.com/)

My friend [Brian](https://github.com/briandant) and I recently argued at [Code Mentors Boston](http://www.meetup.com/Code-Mentors-Boston/) over which is a better Python web framework, Flask or Django?

He made a [Django quickstart](http://django-quickstart.herokuapp.com/) app, thus throwing down The Gauntlet. So, I made [this](https://github.com/garbados/flask-the-gauntlet) in response. It demos writing a webserver, a template, and even using [markdown](http://daringfireball.net/projects/markdown/) to keep your content separate from your templates, because separation of concerns is awesome -- and why I love Flask.

#### Installation

Let's say all you have installed is Python. Cool. Download [install.sh](https://raw.github.com/garbados/flask-the-gauntlet/master/install.sh) and run it like this:

	. ./install.sh

If you're on Windows, use [install_win.sh](https://raw.github.com/garbados/flask-the-gauntlet/master/install_win.sh) instead. Run it like this:

	.\install_win.sh

Now you have the skeleton of a Flask application. Whoo!

If you want to install this application specifically, you'll need [git](http://git-scm.com/). Once you have it installed, run the following to download and setup the app:

	git clone https://github.com/garbados/flask-the-gauntlet.git
	cd flask-the-gauntlet
	virtualenv venv
	source venv/bin/activate # on Windows, "venv\Scripts\activate"
	pip install -r requirements.txt

Now, to start the app, run:

	python app.py

#### Copyleft

Evoked from the Aether by Economancer [Max Thayer](https://github.com/garbados/), 2013. Use, remix, and obliterate at your leisure.