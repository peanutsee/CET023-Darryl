from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import dotenv_values

config = dotenv_values(".env") 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Entry point to the flask backend."""
    return render_template('index.html')
    
@app.route('/makersuite', methods=['GET', 'POST'])
def makersuite():
    return render_template("makersuite.html")

@app.route('/gemini', methods=['GET', 'POST'])
def gemini():
    q = request.form.get('query', "")
    print(q)
    API = config.get('API')

    genai.configure(api_key=API)

    MODEL = genai.GenerativeModel(model_name='gemini-1.5-flash')
    r = MODEL.generate_content(q)
    cleaned_r = r.candidates[0].content.parts[0].text
    print(cleaned_r)
    return render_template('gemini.html', response=cleaned_r)

# Run the App
if __name__ == "__main__":
    app.run(port=8000, debug=True)
