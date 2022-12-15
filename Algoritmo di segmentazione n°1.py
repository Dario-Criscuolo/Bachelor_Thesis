import cv2

filepath_immagine=r'C:\'
myimage = cv2.imread(filepath_immagine)                                      #carica immagine
  
myimage_grey = cv2.cvtColor(myimage, cv2.COLOR_BGR2GRAY)            #converte in grigio
ret,baseline = cv2.threshold(myimage_grey,106,255,cv2.THRESH_TRUNC) 
ret,final_image = cv2.threshold(baseline,105,255,cv2.THRESH_BINARY)
 
final_image = cv2.cvtColor(final_image, cv2.COLOR_GRAY2BGR)         #riconverti in bianco e nero
final_image = 255 - final_image  
cv2.imwrite("immagine_segmentata.jpg", final_image)

