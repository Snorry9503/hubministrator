1) Install MySql

2) Create a DB named "CONDODB"

3) Create an admin user (flag on is_admin) within your MySql cmd

4) CD into the root folder

5) Run this command to start the app

> . start.sh

//These commands will create tables and columns inside your DB

6) Once everything is set, type:

> flask db init

> flask db upgrade

7) Run this command to launch the app on the browser

> flask run