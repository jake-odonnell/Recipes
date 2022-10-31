from distutils.log import debug
from Flask_app import app
from Flask_app.controllers import users

if __name__ == '__main__':
    app.run(debug = True)