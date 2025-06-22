import cv2

#Cambiar ruta para personalizar
img = cv2.imread('/home/dayan/Documentos/Canny/moneda.jpg', 0)
bordeCanny = cv2.Canny(img, 100, 200)

#Muestra la imagen
cv2.imshow('Original', img)
cv2.imshow('Canny', bordeCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
