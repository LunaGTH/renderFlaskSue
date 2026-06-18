from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando en Render, sin modificacion"

if __name__ == "__main__":
    app.run()
