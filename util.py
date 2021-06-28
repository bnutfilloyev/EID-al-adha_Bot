from cv2 import imread
from cv2 import putText
from cv2 import imwrite

from aiogram.types import Message

def putTextOnImage(message:Message)->None:
    img = imread('down_photos/5415106.jpg')
    putText(img, message.text, (590, 1050), 7, 8, (255, 206, 92), 3)
    imwrite("upld_photos/Done.jpg", img)