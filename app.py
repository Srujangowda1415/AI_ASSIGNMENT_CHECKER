from flask import Flask, render_template, request, send_file
import os, json
from utils.ocr import extract_text
from utils.grader import grade_assignment
from utils.pdf_generator import generate_pdf

# Set OpenAI API key directly
os.environ["OPENAI_API_KEY"] = "YOUR-ACTUAL-API-KEY"

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULTS_FILE = "data/results.json"

# Create required directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        roll = request.form["roll"]
        file = request.files["assignment"]
        
        filepath = os.path.join(UPLOAD_FOLDER, f"{roll}.png")
        file.save(filepath)
        
        text = extract_text(filepath)
        marks = grade_assignment(text)
        
        results = {}
        if os.path.exists(RESULTS_FILE):
            with open(RESULTS_FILE) as f:
                results = json.load(f)
        
        results[roll] = marks
        with open(RESULTS_FILE, "w") as f:
            json.dump(results, f, indent=2)
            
        return f"Uploaded. Roll No: {roll}, Marks: {marks}"
        
    return render_template("upload.html")

@app.route("/download-report")
def download():
    path = generate_pdf()
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
