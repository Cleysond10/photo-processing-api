import numpy as np
from matplotlib import pyplot as plt
import cv2
import base64
from io import BytesIO

from utils import base64_to_image


def generate_histogram(base64_string):
    """Function to plt the image histogram by opencv."""
    image = base64_to_image(base64_string)

    CHANNEL = [0]
    HIST_SIZE = [256]
    RANGE = [0, 255]

    histogram = cv2.calcHist(
        np.array(image), CHANNEL, None, HIST_SIZE, RANGE)

    plt.plot(histogram)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    encoded_histogram = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return encoded_histogram
