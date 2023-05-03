import random
from flask import Flask, jsonify, request

app = Flask(__name__)
constant = [1, 2, 3, 4, 5]

@app.route('/', methods=['GET']) #  операцию гет
def get_constant():
    return jsonify(constant)

@app.route('/', methods=['POST']) #  функц пост
def add_constant():
    value = random.randint(0, 100)
    constant.append(value)
    return jsonify({'value': value})

@app.route('/', methods=['DELETE']) # функц делит
def remove_constant():
    if len(constant) == 0:
        return jsonify({'message': 'No constants to delete'})
    else:
        constant.pop()
        return jsonify({'message': 'Last constant deleted'})

if __name__ == '__main__':
    app.run()

"""
fetch('http://localhost:5000/')
  .then(response => response.json())
  .then(data => console.log(data))
######################################
fetch('http://localhost:5000/', { method: 'POST' })
  .then(response => response.json())
  .then(data => console.log(data))
######################################
fetch('http://localhost:5000/', { method: 'DELETE' })
  .then(response => response.json())
  .then(data => console.log(data))
"""


pass
