from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo"

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
