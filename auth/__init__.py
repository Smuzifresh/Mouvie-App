from flask import Blueprint
authblp = Blueprint('auth', __name__)
from . routes import *
