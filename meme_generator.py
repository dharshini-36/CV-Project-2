import cv2

def create_meme(image, text):

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    height, width = image.shape[:2]

    # position for text
    position = (20, height - 20)

    cv2.putText(
        image,
        text,
        position,
        font,
        1,
        (255,255,255),
        2,
        cv2.LINE_AA
    )

    return image
