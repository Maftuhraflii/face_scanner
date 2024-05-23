import cv2

# Inisialisasi Cascade Classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    # Membaca gambar
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces.tolist()

# Contoh penggunaan
if __name__ == "__main__":
    image_path = "example.jpg"
    detected_faces = detect_faces(image_path)
    print("Detected Faces:", detected_faces)
