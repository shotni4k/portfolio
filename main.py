from flask import Flask,render_template
from loguru import logger

app = Flask(__name__, template_folder="template")


@app.route('/')
@app.route('/index')
def get_home_tamplate():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()