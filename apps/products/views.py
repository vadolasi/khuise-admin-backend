from django.http import HttpResponse
from PIL import Image
from urllib.request import urlopen


def image(request):
    image_data = Image.open(
        urlopen(
            f"https://dpkidwvuicjfi.cloudfront.net/media/{request.GET.get('image')}"
        )
    )
    response = HttpResponse(content_type="image/png")
    image_data.save(response, "png")

    return response
