# Deep-Dream
Implementation of TensorFlows deep dream image processing

1. To run unzip Deep-Dream 

2. Open up a terminal and navigate to the now unzipped Deep-Dream folder

3. Enter 'python dream_image.py infilename.jpg outfilename.jpg int(1-10)'
   example: 'python dream_image.py casey-horner-1268624-unsplash.jpg stars_wavy.jpg 1'
   
   The number corresponds to the type of layer you're sending the image through. The numbers correspond to the following layers:
    layer 1: wavy
    layer 2: lines
    layer 3: boxes
    layer 4: circles
    layer 6: dogs, bears, cute animals.
    layer 7: faces, buildings
    layer 8: fish begin to appear, frogs/reptilian eyes.
    layer 10: Monkies, lizards, snakes, ducks
    
    Higher resolution files turn out better but will also take longer to process. 
    JPG and PNG files have been tested and confirmed to work.
    Created and tested in Python 3.6
    
    Dependencies are as follows:
        TensorFlow
        Numpy
        Pillows
        SciPy
