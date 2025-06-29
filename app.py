from flask import Flask, render_template, request
from analytics import analyze_stats
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    graphs = None
    summary = None

    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        summary, graphs = analyze_stats(path)

    return render_template('index.html', summary=summary, graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)