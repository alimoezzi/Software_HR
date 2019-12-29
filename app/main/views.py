from flask import Blueprint, render_template,jsonify
from app import *

main = Blueprint('main', __name__,template_folder='../../templates')


@main.route('/')
@cross_origin()
def index():
    return render_template('main/index.html')


@main.route('/status')
def about():
    return jsonify({'message': 'ok'}), 200
