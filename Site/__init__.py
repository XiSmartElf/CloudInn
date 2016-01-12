from flask import Flask
app = Flask(__name__)
# <<<<<<< HEAD
app.config.from_object('config')

from Site import views




# =======
#
# @app.route("/")
# def main():
#     return "Hello World!"
# >>>>>>> master
