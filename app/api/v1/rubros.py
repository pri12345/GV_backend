from flask import jsonify, render_template, request, redirect, url_for
from app.api.v1 import api_bp
from app.services.rubro_service import RubroService

@api_bp.route('/rubros', methods=['GET'])
def list_rubros():
    rubros = RubroService.get_all_rubros()
    return render_template('rubros.html', rubros=rubros)

@api_bp.route('/rubros/<int:rubro_id>', methods=['GET'])
def get_rubro(rubro_id):
    rubro = RubroService.get_rubro(rubro_id)
    if rubro:
        return jsonify({
            'id': rubro.id,
            'name': rubro.name,
            'categorias': rubro.categorias,
            'items': [{'id': item.id, 'name': item.name} for item in rubro.items]
        })
    return jsonify({'error': 'Rubro not found'}), 404

@api_bp.route('/rubros/add', methods=['GET'])
def show_add_rubro_form():
    return render_template('add_rubro.html')

@api_bp.route('/rubros/add', methods=['POST'])
def add_rubro():
    try:
        name = request.form.get('name')
        id = request.form.get('id')
        categorias = request.form.get('categorias')

        if not id:
            return render_template('add_rubro.html', error='ID is required')

        try:
            id = int(id)
        except ValueError:
            return render_template('add_rubro.html', error='ID must be a number')

        rubro, error = RubroService.create_rubro(
            name=name,
            id=id,
            categorias=categorias
        )

        if error:
            return render_template('add_rubro.html', error=error)

        return redirect(url_for('api.list_rubros'))

    except Exception as e:
        return render_template('add_rubro.html', error=str(e)) 