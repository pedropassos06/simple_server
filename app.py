from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Congrats on your first web server!'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=1025) #change the port to the port assigned to your project


