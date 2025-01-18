from flask import Flask, send_file, render_template
from qr_generator import generate_qr

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/qr")
def get_qr():
    buffer = generate_qr()
    return send_file(buffer, mimetype='image/png')

if __name__ == "__main__":
    app.run()