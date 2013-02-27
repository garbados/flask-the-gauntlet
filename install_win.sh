easy_install virtualenv
mkdir the_gauntlet_has_been_thrown
cd the_gauntlet_has_been_thrown
virtualenv venv
venv\Scripts\activate
pip install flask, markdown
pip freeze > requirements.txt
mkdir templates static static\css
touch app.py templates\index.html static\css\style.css