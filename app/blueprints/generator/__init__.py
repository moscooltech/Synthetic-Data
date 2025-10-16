from flask import Blueprint

generator = Blueprint('generator', __name__)

from . import routes
