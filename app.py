# %%  Imports and initial configurations
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from models import db, Item, Sale  # Assuming models.py (in repo) contains the SQLAlchemy models

app = Flask(__name__)
CORS(app)

#%% Database configuration (later switch to PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#%% Routing

@app.route('/')   # Simple front-end to visualize
def home():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])

def hello():
    return jsonify({"message": "Probando el backend con Flask"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)