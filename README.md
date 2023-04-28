# CCTV-Small-Object-Detection
This repository contains the datasets gathered for my final year project.  
It also contains the weights produced by training YOLOv7 on augmented version of the datasets and the python code used to augment them.  
  
The python scripts function by being added to the folder you want to run them in and then running them.  
The compression python file will compress images to 10% of their original quality and writes the new images to a new compressed folder.  
The DataAugmentor.py script creates horizontally flipped and black and white versions of every image in the images folder in its diretory. It also copies and modifies the YOLOv7 labels in the associated labels folder.  
  
The weights can be used with a fork of the YOLOv7 repository and can perform inference on test images.
