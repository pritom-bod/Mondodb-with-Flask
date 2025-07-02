from flask import Flask, redirect, url_for
from routes.author_routes import author_bp
from routes.post_routes import post_bp

app = Flask(__name__)

app.register_blueprint(author_bp)
app.register_blueprint(post_bp)

# root url redirect to authors
@app.route("/")
def home():
    return redirect(url_for("author.list_authors"))

if __name__ == "__main__":
    app.run(debug=True)
