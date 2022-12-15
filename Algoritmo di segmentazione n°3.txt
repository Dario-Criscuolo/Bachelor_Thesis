#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>
using namespace cv;
using std::cout;

int threshold_value = 0;
int threshold_type = 3;
int const max_value = 255;
int const max_type = 4;
int const max_binary_value = 255;

Mat src, src_gray, dst;
const char* window_name = "Threshold";
const char* trackbar_type = "Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted";
const char* trackbar_value = "Value";

static void Threshold_Demo(int, void*)
{   threshold(src_gray, dst, threshold_value, max_binary_value, threshold_type);
    imshow(window_name, dst);                                 //visualizza l'immagine
    imwrite("immagine_segmentata.jpg", dst);                               //salva immagine
}
int main()
{   String imageName("nomeimmagine.jpg"); 
    src = imread(samples::findFile(imageName), IMREAD_COLOR);//carica l'immagine

    cvtColor(src, src_gray, COLOR_BGR2GRAY);                 //converti l'immagine in grigio
    namedWindow(window_name, WINDOW_AUTOSIZE);               //crea una finestra far vedere immagine
    imwrite("immagine_grigia.jpg", src_gray);
    createTrackbar(trackbar_value,                           //crea una Trackbar per tipo di Threshold
        window_name, &threshold_type,
        max_type, Threshold_Demo);                           
    createTrackbar(trackbar_value,                           //crea una Trackbar per valore di Threshold
        window_name, &threshold_value,
        max_value, Threshold_Demo);                          

    Threshold_Demo(0,0);                                     //chiami la funzione 
    waitKey();                                               //evita che la finestra si chiuda subito    
}