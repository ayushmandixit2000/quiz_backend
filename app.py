from flask import Flask
from flask_cors import CORS
from routes import quiz_routes

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Register routes
app.register_blueprint(quiz_routes)

if __name__ == "__main__":
    app.run()