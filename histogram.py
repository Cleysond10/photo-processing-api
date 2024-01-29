import os
from matplotlib import pyplot as plt
import cv2


def generate_histogram(path):
    """Function to plt the image histogram by opencv."""
    filename = os.path.basename(path).split('.')[0]
    image = cv2.imread(path)
    CHANNEL = [0]
    HIST_SIZE = [256]
    RANGE = [0, 255]
    histogram = cv2.calcHist(
        image, CHANNEL, None, HIST_SIZE, RANGE)
    plt.subplot(111), plt.plot(histogram)
    plt.savefig(f'{filename}_hist')
    plt.clf()
