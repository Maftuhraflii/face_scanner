from flask import Flask, request, jsonify, render_template
from face_recognition import detect_faces

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_faces', methods=['POST'])
def detect_faces_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    faces = detect_faces(file)
    return jsonify(faces)

if __name__ == '__main__':
    app.run(debug=True)
