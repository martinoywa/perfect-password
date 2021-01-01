from flask import Flask

"""
Initialize application
"""
app = Flask(__name__)

from .views import main
app.register_blueprint(main)
