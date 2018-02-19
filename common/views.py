"""
通过表单传进一张图片
保存并返回图片url
"""

from django.http import JsonResponse

from .utils import save_image


def upload_image(request):
    img = request.FILES.get('image')
    path = save_image(img)
    return JsonResponse({'uploadSuccess': 'OK', 'imgPath': path}, status=201)
