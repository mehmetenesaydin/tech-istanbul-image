import cv2
import numpy as np

def apply_filter(image_path, filter_name):
    image = cv2.imread(image_path)
    
    if filter_name == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    elif filter_name == 'invert':
        return cv2.bitwise_not(image)
    
    elif filter_name == 'brightness':
        return cv2.convertScaleAbs(image, alpha=1.2, beta=50)
    
    elif filter_name == 'sepia':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_image = cv2.transform(image, sepia_filter)
        sepia_image = np.clip(sepia_image, 0, 255)
        return sepia_image.astype(np.uint8)
    
    elif filter_name == 'gaussian_blur':
        return cv2.GaussianBlur(image, (15, 15), 0)
    
    elif filter_name == 'sharpen':
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)
    
    elif filter_name == 'edge_detection':
        return cv2.Canny(image, 100, 200)
    
    elif filter_name == 'autumn':
        return cv2.applyColorMap(image, cv2.COLORMAP_AUTUMN)
    
    elif filter_name == 'emboss':
        kernel = np.array([[ -2, -1, 0],
                           [ -1, 1, 1],
                           [ 0, 1, 2]])
        embossed_image = cv2.filter2D(image, -1, kernel)
        return cv2.convertScaleAbs(embossed_image)
    
    elif filter_name == 'sketch':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inv = cv2.bitwise_not(gray)
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256)
        return sketch
    
    elif filter_name == 'cartoon':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        smooth = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon
    
    return image
