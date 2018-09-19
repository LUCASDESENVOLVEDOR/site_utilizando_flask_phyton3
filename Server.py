from flask import Flask
from flask import render_template
from flask import request


#codigo para abrir os arquivos estaticos, adicionei todos na pasta "principal".
App = Flask(__name__, static_folder='principal', static_url_path='')

@App.route("/", methods=["GET"])
@App.route("/home", methods=["GET"])
def Home():
    return render_template("index.html")

    
if __name__ == "__main__":
    App.run(port=80)