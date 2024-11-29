#mengimpor library open cv untuk pengolahan gambar dan video
import cv2

# Load the cascade(digunakan untuk mendeteksi wajah)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Untuk merekam video dari webcam. 
cap = cv2.VideoCapture(0)
# Untuk menggunakan file video sebagai input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # untuk membaca bingkainya
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # untuk Mendeteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Gambar persegi panjang di sekitar setiap sisinya
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Berhenti jika tombol escape ditekan
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# menutup koneksi kamera atau file video
cap.release()