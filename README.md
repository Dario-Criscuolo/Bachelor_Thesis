# Dario-s-thesis
L’obiettivo di questa tesi di laurea è quello di fornire un metodo per l'estrazione di una parte specifica di un'immagine, 
anche di bassa qualità, ricavando successivamente la grandezza reale dell'oggetto che è scopo di analisi.
Nel concreto prenderò delle immagini dove sono presenti tronchi visti da davanti all'interno di uno sfondo generico,
per poi estrarre con la segmentazione l'area dei tronchi e ottenere così il volume totale dei tronchi all'interno della fotografia.


# Sommario Tesi
Computer e algoritmi sono diventati utili in tutti gli aspetti della nostra vita quotidiana, e questi utilizzano spesso le immagini.
Molti settori infatti impiegano la fotografia, strumento immediato e alla portata di tutti, per effettuare computazioni e misurazioni.
Nella falegnameria ad esempio, data una fotografia o un'immagine, è necessario segmentarla ottenendo solo la porzione necessaria dell'immagine 
(in una fotografia di alcuni tronchi nella foresta l'obiettivo è estrarre solo la porzione di tronchi o legname, togliendo così lo sfondo)
su cui poi verrà effettuata la misura (ad esempio il calcolo del volume di tale legname). Purtroppo uno dei problemi principali è la qualità di tali immagini,
che nella maggior parte dei casi, non è abbastanza elevata da permettere una perfetta distinzione degli oggetti. Ne consegue quindi, 
che estrarre dati e misure dalle immagini, è un task difficile, ma d'interesse rilevante nell'area della Image Analysis e più in generale della 
Computer Science.


# Guida all'utilizzo degli algoritmi
Inserisci l'immagine di cui vuoi sapere il volume totale dei tronchi in uno dei 3 algoritmi di segmentazione
(riferirsi al file tesi per decidere quale sia il più adatto alla propria situazione a pag.15).
Poi inserire l'immagine segmentata, la parte tagliata (tesi a pag. 22) insieme a l'area del tronco di cui sapevamo area e lunghezza media tronchi 
all'interno dell'algoritmo di calcolo per ottenere il volume totale dei tronchi.



# Input che prendono gli algoritmi
-Immagine con i tronchi,
-lunghezza media dei tronchi,
-valore dell'area reale di un tronco, Immagine ritagliata del tronco di cui ho il valore dell'area
