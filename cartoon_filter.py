import cv2

def cartoonify(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # blur
    gray = cv2.medianBlur(gray, 5)

    # edge detection
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # smooth colors
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # combine
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon
