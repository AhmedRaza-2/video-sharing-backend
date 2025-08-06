from flask import Flask
from routes.videos import videos_bp
from routes.auth import auth_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(videos_bp, url_prefix="/api/videos")
app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.route('/')
def index():
    return {"status": "Video Sharing App is running"}

if __name__ == "__main__":
    app.run(debug=True)
