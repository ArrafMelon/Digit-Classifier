import cv2
def img_transform(img_path):
    ## Grayscaling
    img_path = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ## Invert bitmaps to increase contrast between pixels
    img_path = cv2.bitwise_not(img_path)
    ## resize to 8x8
    img_path = cv2.resize(img_path,(8,8))
    ## Flatten into 1D array
    img_path = img_path.flatten().reshape(1,-1)
    return img_path