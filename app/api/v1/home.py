from flask import jsonify, render_template, redirect, url_for
from app.api.v1 import api_bp

@api_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api_bp.route('/informe')
def show_informe():
    return render_template('informe.html')

@api_bp.route('/understocked')
def show_understocked():
    return render_template('understocked.html')

@api_bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Probando el backend con Flask"}) 