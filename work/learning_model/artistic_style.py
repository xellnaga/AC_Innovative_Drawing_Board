import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
import os
import time
import sys
'''PATH'''
ROOT_DIR = os.path.abspath("")
content_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/belfry.jpg'
style_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/style.jpg'
style_predict_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/prediction.tflite'
style_transform_path = 'C:/Users/user/PycharmProjects/AC_Innovative_Drawing_Board/resource/tflite/transfer.tflite'

def run_style_predict(preprocessed_style_image):
  # Load the model.
  interpreter = tflite.Interpreter(model_path=style_predict_path)

  # Set model input.
  interpreter.allocate_tensors()
  input_details = interpreter.get_input_details()
  interpreter.set_tensor(input_details[0]["index"], preprocessed_style_image)

  # Calculate style bottleneck.
  interpreter.invoke()
  style_bottleneck = interpreter.tensor(
      interpreter.get_output_details()[0]["index"]
      )()

  return style_bottleneck


def run_style_transform(style_bottleneck, preprocessed_content_image):
  # Load the model.
  interpreter = tflite.Interpreter(model_path=style_transform_path)

  # Set model input.
  input_details = interpreter.get_input_details()
  interpreter.allocate_tensors()

  # Set model inputs.
  interpreter.set_tensor(input_details[0]["index"], preprocessed_content_image)
  interpreter.set_tensor(input_details[1]["index"], style_bottleneck)
  interpreter.invoke()

  # Transform content image.
  stylized_image = interpreter.tensor(
      interpreter.get_output_details()[0]["index"]
      )()

  return stylized_image

# Stylize the content image using the style bottleneck.

def preprocess_image(image, target_dim):
    print(image.shape)
    center = [image.shape[0] / 2 , image.shape[1] / 2]
    h = image.shape[0]
    w = image.shape[1]
    short_dim = min(h, w)
    scale = target_dim / short_dim
    new_h = scale * h
    new_w = scale * w
    x = center[1] - w / 2
    y = center[0] - h / 2
    image = cv2.resize(image, (int(new_w), int(new_h)), interpolation=cv2.INTER_CUBIC)

    crop_img = image[int(y):int(y + target_dim), int(x):int(x + target_dim)]

    return crop_img


content_img = cv2.imread(content_path)
style_img = cv2.imread(style_path)

content_img = preprocess_image(content_img,384)#cv2.resize(content_img, (384, 384), interpolation = cv2.INTER_CUBIC)
style_img = preprocess_image(style_img,256)#cv2.resize(style_img,(256, 256), interpolation = cv2.INTER_CUBIC)
cv2.imshow("content_img",content_img)
cv2.imshow("style_img",style_img)
cv2.waitKey(0)
content_img = content_img.astype(np.float32)
style_img = style_img.astype(np.float32)

preprocessed_content_image = np.expand_dims(content_img, axis=0)
preprocessed_style_image = np.expand_dims(style_img, axis=0)

print('Style Image Shape:', preprocessed_style_image.shape)
print('Content Image Shape:', preprocessed_content_image.shape)

style_bottleneck = run_style_predict(preprocessed_style_image)
print('Style Bottleneck Shape:', style_bottleneck.shape)
stylized_image = run_style_transform(style_bottleneck, preprocessed_content_image)

stylized_image = np.squeeze(stylized_image, axis=0)

stylized_image = stylized_image * 255.0
stylized_image = stylized_image.astype(np.uint8)


cv2.normalize(stylized_image,  stylized_image, 0, 255, cv2.NORM_MINMAX)


cv2.imshow("stylized_image",stylized_image)
cv2.waitKey(0)