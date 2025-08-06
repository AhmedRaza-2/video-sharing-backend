from flask import Blueprint, request, jsonify
from services.azure_blob import upload_video_to_blob
from models.database import save_video_metadata, get_all_videos

videos_bp = Blueprint('videos', __name__)

@videos_bp.route('/upload', methods=['POST'])
def upload_video():
    file = request.files.get('file')
    title = request.form.get('title')
    genre = request.form.get('genre')
    age_rating = request.form.get('age_rating')
    user_id = request.form.get('user_id')

    if not file or not title:
        return {"error": "Missing data"}, 400

    blob_url = upload_video_to_blob(file)

    video_doc = {
        "title": title,
        "genre": genre,
        "age_rating": age_rating,
        "creator_id": user_id,
        "video_url": blob_url
    }

    save_video_metadata(video_doc)

    return {"message": "Uploaded successfully", "url": blob_url}

@videos_bp.route('/all', methods=['GET'])
def all_videos():
    return jsonify(get_all_videos())
