from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('multiplication.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or 'numbers' not in data:
        return jsonify({'error': 'No numbers provided'}), 400
    numbers = data['numbers']
    result = sum(numbers)
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if not data or 'numbers' not in data:
        return jsonify({'error': 'No numbers provided'}), 400
    numbers = data['numbers']
    result = 1
    for number in numbers:
        result *= number
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
