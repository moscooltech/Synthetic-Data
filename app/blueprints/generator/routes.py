from flask import render_template
from . import generator


@generator.route('/')
def index():
    return render_template('generator.html')
