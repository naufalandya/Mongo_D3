from flask import Flask, make_response
from flask_cors import CORS
from controllers import controller_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(controller_bp, url_prefix='/api/v1')

@app.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'public, max-age=300' 
    return response

if __name__ == '__main__':
    app.run(debug=True, port=3766)
