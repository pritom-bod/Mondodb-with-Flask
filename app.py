from flask import Flask
from routes.author_routes import author_bp
from routes.post_routes import post_bp

app = Flask(__name__)

# register routes
app.register_blueprint(author_bp)
app.register_blueprint(post_bp)

if __name__ == "__main__":
    app.run(debug=True)
