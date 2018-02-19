"""
保存到static/images/{year}{month}/uuid[:22]timstamp.ext
"""

import time
import os
from datetime import datetime
from uuid import uuid4
from myBlog.settings import BASE_DIR


def genr_image_path(img):
    img_dir = os.path.join(BASE_DIR, 'static/images/%d%d/' % (datetime.now().year, datetime.now().month))
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    name = uuid4().hex[:22] + str(int(time.time()))
    ext = os.path.splitext(img.name)[1]
    return img_dir + name + ext


def save_image(img):
    path = genr_image_path(img)
    with open(path, 'wb') as f:
        f.write(img.read())
    return path


