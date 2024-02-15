"""Module providing a photo classification."""
import numpy as np
from scipy import stats

from utils import base64_to_image


def get_conclusion(mean, median, mode):
    """Function getting conclusion from stats."""
    if mean == median == mode:
        return 'CONCLUSÃO: NORMAL'
    if mean > median > mode:
        return 'CONCLUSÃO: ESCURA'
    if mean < median < mode:
        return 'CONCLUSÃO: CLARA'
    if mode > mean and mode > median:
        return 'CONCLUSÃO: ?CLARA'
    if mode < mean and mode < median:
        return 'CONCLUSÃO: ?ESCURA'

    return 'CONCLUSÃO: ??'


def get_photo_classification(photo):
    """Function getting image classification from photo."""
    image = base64_to_image(photo)

    if image:
        try:
            mean = np.mean(image, axis=None)
            median = np.median(image, axis=None)
            mode = stats.mode(image, axis=None, keepdims=False).mode

            return get_conclusion(mean, median, mode)
        except Exception as e:
            print(f"Error: {e}")
            return 'Error: Could not get image stats.'
    else:
        return 'Error: Invalid image.'
