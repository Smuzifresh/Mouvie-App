from flask import Blueprint
mainblp = Blueprint('main', __name__)
from .routes import *