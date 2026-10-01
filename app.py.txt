from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Women Safety App is Working!</h1><p>Emergency: 100 | Helpline: 1091</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)