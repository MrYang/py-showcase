from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/post', methods=['POST'])
def post():
    return jsonify({'code': 200, 'msg': 'ok'})


if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, port=5000)
