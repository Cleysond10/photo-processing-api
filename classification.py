"""Module providing a photo classification."""
import base64
from io import BytesIO
from PIL import Image
import numpy as np
from scipy import stats


def base64_to_image(base64_string):
    """Function getting an image from base64."""
    try:
        image_data = base64.b64decode(base64_string)
        image_buffer = BytesIO(image_data)
        image = Image.open(image_buffer)

        return image
    except Exception as e:
        print(f"Error: {e}")
        return 'Error: Could not convert base64 to image.'


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
