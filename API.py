import io
import json

from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

#initialization of app and pretrained model
app = Flask(__name__)
imagenet_class_index = json.load(open('imagenet_class_index.json'))
model = models.densenet121(pretrained=True)
model.eval()

# Converting into a 3D matrix and normalizing pixels.
def transform_image(image_bytes):
	#used transforms from torchvision library and built a transform pipeline
	#Since the DenseNet model requires the image to be of 3 channel RGB image of size 224 x 224
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    #normalised the image tensor with the required mean and standard deviation values
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

# get image label.
def get_prediction(image_bytes):
	#calling the transform_image function to convert the image
    tensor = transform_image(image_bytes=image_bytes)
    #passing the transformed image to the densenet121 tensor model
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    #getting the predicted label
    predicted_idx = str(y_hat.item())
    #returning the class id and class name of the predicted label from the json file
    return imagenet_class_index[predicted_idx]

# Function called with a HTTP 'POST' request.
@app.route('/upload', methods=['POST'])
def upload():
	#if the server gets a post request, it will store the image file and run the densenet on it
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        #extracting the label from the json file
        return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == '__main__':
	#running the application on localhost with debugging
    app.run(host = "0.0.0.0", debug = True)