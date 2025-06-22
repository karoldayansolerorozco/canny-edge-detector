import cv2

img = cv2.imread('/home/dayan/Documentos/Canny/moneda.jpg', 0)
bordeCanny = cv2.Canny(img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Canny', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
