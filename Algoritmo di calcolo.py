import cv2

filepath_immagine=r'C:\'
img_data = cv2.imread(filepath_immagine)                                 #carica immagine ritagliata
hh, ww = img_data.shape[:2]                                     #prende larghezza e altezza dell'immagine

filepath_immagine=r'C:\'
imgtot = cv2.imread(filepath_immagine)                                   #carica immagine intera
hh1, ww1 = imgtot.shape[:2]                                     #prende larghezza e altezza dell'immagine
print(hh1)
print(ww1)

ave = cv2.mean(img_data)[0]/255                                 #prendo media di pixel bianchi(average)
totpixreale = ave*hh*ww                                         #calcolo numero totale di pixel bianchi nella foto piccola

area_data=0.1257                                                #valore reale dato
pixel_metri=area_data/totpixreale                               #calcolo quando vale un pixel bianco come valore reale
ave1 = cv2.mean(imgtot)[0]/255                                  #prendo media di pixel bianchi(average)
totpixel = ave1*hh1*ww1                                         #totale pixel nella foto grossa
area_finale=pixel_metri*totpixel                                #trovo area reale dei pixel bianchi nella foto grossa

lunghezza_tronchi=0.9                                             #valore dato
volume_finale=area_finale*lunghezza_tronchi                     #trovo il risultato finale
print(volume_finale)                           



