from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users/<string:name>')
def users(name = None):
    return "This is {name}".format(name = name)

# if error occur, change host to 127.0.0.1
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
    