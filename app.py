# %%  Imports
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])

def hello():
    return jsonify({"message": "Probando el backend con Flask"})

if __name__ == '__main__':
    app.run(debug=True)