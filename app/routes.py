from flask import Blueprint, jsonify
from app.service import fetch_latest_news

bp = Blueprint('api', __name__)


@bp.route('/api/latest_news', methods=['GET'])
def get_latest_news():
    try:
        items = fetch_latest_news()
        return jsonify([item.__dict__ for item in items])
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
