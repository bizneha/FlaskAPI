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

app = Flask(__name__)#creates an instance of the Flask class

@app.route('/')# decorator # base page
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['GET', 'POST']) #route now accepts both GET and POST requests
def add_numbers():
    if request.method == 'POST': #create  
        a = request.form.get('a', type=int) #to retrieve a and b from the form data submitted by the user.
        b = request.form.get('b', type=int)
        if a is None or b is None:
            return jsonify(error="Please provide both 'a' and 'b' as form inputs"), 400 # return a JSON response with an error message and a 400 status code.
        result = a + b #If both a and b are provided and valid, you calculate their sum and return the result as a JSON response.
        return jsonify(result=result) 
    return render_template('add_form.html',result=result)

if __name__ == "__main__": #
    app.run(debug=True)




#class(write code in oops concept) add,subtract(any no of inputs could be variable )