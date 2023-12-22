#import packet
import cv2

#Membaca file gambar aril.jpg yang berada dalam folder yang sama dengan file ReadImageData.py
img = cv2.imread("aril.jpg")

#Menampilkan data piksel citra
print('Image', img)

#Menampilkan Citra
cv2.imshow("Gambar aril Original", img)

cv2.waitKey(0)
cv2.destroyWindow()

