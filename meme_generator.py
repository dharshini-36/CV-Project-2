import cv2
import random

# List of random meme captions
captions = [
    "When exam tomorrow but you start studying today",
    "Me pretending to understand the lecture",
    "When the code works but you don't know why",
    "Debugging for 5 hours and the problem was a missing comma",
    "When WiFi disconnects during submission",
    "When teacher says this will come in exam",
    "When your code runs successfully on first try",
    "Me after fixing one bug and creating three new ones"
]

# Function to generate random caption
def generate_caption():
    return random.choice(captions)

# Function to add caption on image
def create_meme(image, text):

    font = cv2.FONT_HERSHEY_SIMPLEX
    height, width = image.shape[:2]

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
