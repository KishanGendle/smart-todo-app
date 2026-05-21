from flask import Flask, render_template
from flask_session import Session
from dotenv import load_dotenv
from config.db import mongo
from routes.auth_routes import auth
from routes.task_routes import task
import os

load_dotenv()

app = Flask(__name__)

# Secret Key
app.secret_key = os.getenv("SECRET_KEY")

# MongoDB Config
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Session Config
app.config["SESSION_TYPE"] = "filesystem"

# Initialize MongoDB
mongo.init_app(app)

# Initialize Session
Session(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(task)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)