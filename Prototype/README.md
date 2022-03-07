## Setup (mac/linux)
### Flask
1. Ensure you are in the `Prototype/` folder.
2. Run `python3 -m venv venv` to setup a virtual environment 
3. Run `source venv/bin/activate` to activate the virtual environment
4. Run `python3 -m pip install -r requirements.txt` to install Flask & Flask-WTF
5. Run `export FLASK_DEBUG=True` so the application reloads when you change code
6. Run `python3 -m flask run --host 0.0.0.0` to run the application
7. Go to http://127.0.0.1:5000/
### SASS & JS

1. Ensure you are in the `Prototype/` folder.
1. Run `npm i -g sass` to install SASS globally if you haven't used it before.
2. Run `npm i` to install webpack/babel
3. Run `npm start-sass` to start SASS
4. in a new terminal, go to the `Prototype/` folder again and run `npm run start-scripts` to run webpack