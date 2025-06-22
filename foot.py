import cv2
import requests
import base64
import numpy as np
import os 

GROQ_API_KEY = ""
GROQ_API_KEY = ""

def detect_faces(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 