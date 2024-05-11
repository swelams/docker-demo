from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    return 'Hello, World! from sprint30 a7la msa 3leko'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)

