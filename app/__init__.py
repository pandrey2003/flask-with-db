from flask import Flask, render_template

from .frontended import frontended
from .servered import servered

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(frontended)
app.register_blueprint(servered)


@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404
