from flask import Flask, request, jsonify, render_template

class MathAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.add_routes()

    def add_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/add', 'add', self.add, methods=['POST'])
        self.app.add_url_rule('/multiply', 'multiply', self.multiply, methods=['POST'])

    def index(self):
        return render_template('index.html')

    def add(self):
        data = request.get_json()
        if not data or 'numbers' not in data:
            return jsonify({'error': 'No numbers provided'}), 400
        numbers = data['numbers']
        result = sum(numbers)
        return jsonify({'result': result})

    def multiply(self):
        data = request.get_json()
        if not data or 'numbers' not in data:
            return jsonify({'error': 'No numbers provided'}), 400
        numbers = data['numbers']
        result = 1
        for number in numbers:
            result *= number
        return jsonify({'result': result})

    def run(self, debug=True):
        self.app.run(debug=debug)

if __name__ == '__main__':
    math_api = MathAPI()
    math_api.run()
