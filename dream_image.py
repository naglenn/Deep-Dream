from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image

# determines layer to apply to image
layerTensor = model.layer_tensors[1]

# instantiates img filename and img object
filename = "casey-horner-1268624-unsplash.jpg"
img = load_image(filename='{}'.format(filename))

img_result = recursive_optimize(layer_tensor=layerTensor, image=img,
                                # determines image clarity
                                num_iterations=20, step_size=1.0, rescale_factor=0.5,
                                # How many passes over the data. More passes means more granular gradients
                                num_repeats=8, blend=0.2)

img_result = np.clip(img_result, 0.0, 255.0)
img_result = img_result.astype(np.uint8)
result = PIL.Image.fromarray(img_result, mode='RGB')
result.save('dream_image_out.jpg')
result.show()
