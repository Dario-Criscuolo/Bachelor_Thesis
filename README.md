# Bachelor Thesis
The objective of this thesis is to provide a method for the extraction of a specific part of an image, even of low quality, and subsequently obtain the actual size of the target that is the object of analysis.
In practice, I will take images where there are logs seen from the front within a generic background, and firstly extract the area of the logs by segmentation and thus obtain the total volume of the logs within the photograph.

# Thesis Summary
Computers and algorithms have become useful in all aspects of our daily lives, and these often make use of images. In fact, many sectors employ photography, an immediate tool within everyone's reach, to perform computations and measurements.
In carpentry for example, given a photograph or image, it is necessary to segment it to obtain only the necessary portion of the image (in a photograph of some logs in the forest, the aim is to extract only the portion of logs or timber, thus removing the background) on which the measurement (e.g. the calculation of the volume of that timber) will then be made. Unfortunately, one of the main problems is the quality of such images, which, in most cases, is not high enough to allow a perfect distinction between the objects. It follows then, that extracting data and measurements from images, is a difficult task, but one of relevant interest in the area of Image Analysis and Computer Science more generally.

# Guide to using the algorithms
Insert the image whose total log volume you want to know into one of the 3 segmentation algorithms (refer to the thesis file to decide which one is best for your situation on page 15). Then enter the segmented image, the cut part (thesis on p. 22) together with the log area of which we knew the area and the average log length into the calculation algorithm to obtain the total log volume.

# Input taken by the algorithms
* Image with logs
* Average log length
* Actual log area value
* Cropped image of the log whose area value I have
