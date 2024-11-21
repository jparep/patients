from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    return "Patients App Running!"

if __name__ == "__main__":
    app.run(debug=True)
