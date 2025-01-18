from flask import Flask, Response
from qr_generator import generate_qr

app = Flask(__name__)  

@app.route("/")
def get_qr():

    qr_image = generate_qr()
    return Response(qr_image, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True) 