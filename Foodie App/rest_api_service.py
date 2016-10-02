from flask import Flask, jsonify
from translate_image_service import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

ALLOWED_ORIGINS = "*"
CORS(app, resources={r"/api/*": {"origins": ALLOWED_ORIGINS}})

@app.route('/foodieapi/')
@cross_origin()
def index():
    searchKey = request.form["key"]
    headers("Content-Type", "application/json")
    return jsonify(mainToRun(searchKey))
    
if __name__=="__main__":
	app.run(debug=True, port=9999)
