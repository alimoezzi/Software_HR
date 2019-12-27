from flask import Blueprint, render_template
from app import *

main = Blueprint('main', __name__,template_folder='../../templates')


@main.route('/')
@cross_origin()
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    return render_template('main/about.html')
