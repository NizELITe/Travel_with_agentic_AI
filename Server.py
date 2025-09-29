from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from router import app as graph_app

flask_app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(flask_app)

# Health check
@flask_app.route("/health")
def health():
    return jsonify({"status": "ok"})

# Web frontend
@flask_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        if not query:
            return render_template("index.html", error="Please enter a query.")

        state = {"query": query, "hotel_result": None, "flight_result": None}
        res = graph_app.invoke(state)

        return render_template("results.html", query=query, results=res)

    return render_template("index.html")

# API endpoint
@flask_app.route("/api/query", methods=["POST"])
def api_query():
    data = request.get_json(silent=True) or {}
    query = data.get("query")
    if not query:
        return jsonify({"error": "query required"}), 400

    state = {"query": query, "hotel_result": None, "flight_result": None}
    res = graph_app.invoke(state)
    return jsonify(res)

if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=5000)
