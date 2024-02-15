import base64
from io import BytesIO
from PIL import Image


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
