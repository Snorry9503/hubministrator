pip install virtualenv
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv my-venv
workon my-venv
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
