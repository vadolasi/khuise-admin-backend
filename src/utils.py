import base64
import uuid

from django.core.files.base import ContentFile


def base64_2image(base64string, exists=False):
    image_format, imgstr = base64string.split(';base64,')

    if exists:
        return ContentFile(base64.b64decode(imgstr))

    ext = image_format.split('/')[-1]
    name_ext = f'{uuid.uuid4()}.{ext}'

    return ContentFile(base64.b64decode(imgstr), name=name_ext)
