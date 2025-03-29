from flask import Blueprint, request, jsonify
from .utils import load_data
from .services import search_operadoras

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/api/search', methods=['GET'])
def search():
    try:
        query = request.args.get('q', '').strip()
        if not query or len(query) < 3:
            return jsonify({"error": "O termo de busca deve ter pelo menos 3 caracteres", "status": 400}), 400

        df = load_data()
        results = search_operadoras(query, df)

        return jsonify({"status": 200, "query": query, "count": len(results), "results": results})
        
    except Exception as e:
        return jsonify({"error": str(e), "status": 500}), 500
