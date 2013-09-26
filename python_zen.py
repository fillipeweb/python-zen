import this
from flask import Flask
from flask import render_template

app = Flask(__name__)
zen = "".join([this.d.get(this.c, this.c) for this.c in this.s])

@app.route("/")
def index():
	return render_template('content.html', zen=zen)