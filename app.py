from flask import Flask

app = Flask(__main__)

@app.route("/") #this is your "home" route
def index():
    return "Congrats, this is the beginning of a great server!"

if __name__ = '__main__':
    app.run(host="127.0.0.1", port=1025) #change the port to the port assigned to your project
