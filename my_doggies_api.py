from flask import Flask, jsonify
from my_doggies import woof
app = Flask(__name__)


@app.route('/api/my_doggies/<name>', methods=["GET"])
def return_description(name):
	return jsonify({'my_dog: ':woof(name)})
