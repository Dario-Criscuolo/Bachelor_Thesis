import cv2
import numpy as np

filepath_immagine=r'C:\'
img = cv2.imread(filepath_immagine)                                      #carica immagine 

lower = np.array([180, 180, 180])                               #crei limiti
upper = np.array([255, 255, 255])

thresh = cv2.inRange(img, lower, upper)                         #tutto ciò sopra a limite diventa nero e sotto diventa bianco
  
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))  #prendi pixel  nero
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)       #pulisce immagine
mask = 255 - morph                                              #inverte i colori

cv2.imwrite("immagine_segmentata.jpg", mask)                           #salvi il risultato
