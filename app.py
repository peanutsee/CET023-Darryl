from flask import Flask
from flask import request, render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Entry point to the flask backend."""
    return render_template('index.html')
    
    
# Run the App
if __name__ == "__main__":
    app.run(port=8000, debug=True)