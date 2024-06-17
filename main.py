# from flask import Flask, jsonify,request

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# # @app.route('/add')
# # def sum(a, b):
# #     return a + b

# @app.route('/add')
# def add_numbers():
#     a = request.args.get('a', type=int)
#     b = request.args.get('b', type=int)
#     if a is None or b is None:
#         return jsonify(error="Please provide both 'a' and 'b' as query parameters"), 400
#     result = a + b
#     return jsonify(result=result)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        a = request.form.get('a', type=int)
        b = request.form.get('b', type=int)
        if a is None or b is None:
            return jsonify(error="Please provide both 'a' and 'b' as form inputs"), 400
        result = a + b
        return jsonify(result=result)
    return render_template('add_form.html')

if __name__ == "__main__":
    app.run(debug=True)
