from collections import OrderedDict
import random

from django.utils import timezone

from .models import Post, Tag, FriendLink, Contact


def get_hot_posts(size=5):
    posts = Post.objects.all()[:size]
    return posts


def pageonhole_count():
    """归档统计"""
    now_year = timezone.now().year
    counts = OrderedDict()
    month_mapper = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六',
                    7: '七', 8: '八', 9: '九', 10: '十', 11: '十一', 12: '十二'}
    for year in range(now_year, 2016, -1):
        for month in range(12, 0, -1):
            if Post.objects.filter(created_time__year=year,
                                   created_time__month=month).count() > 0:
                name = '%d年%s月' % (year, month_mapper[month])
                counts[name] = [year, month]
    return counts


def generate_tag_cloud():
    """生成标签云"""
    tags = Tag.objects.all()
    label_types = ['default', 'primary', 'danger', 'info', 'warning']
    backup = []
    tag_cloud = {}
    for tag in tags:
        if not label_types:
            label_types, backup = backup, label_types
        label = label_types.pop(random.randint(0, len(label_types)-1))
        backup.append(label)
        count = Post.objects.filter(tags=tag).count()
        tag_cloud[tag.name] = [label, count]
    return tag_cloud


def friend_links():
    """获取友链"""
    return FriendLink.objects.all()


def social_contacts():
    """获取社交联系方式"""
    return Contact.objects.all()


def newest_post():
    return Post.objects.order_by('-created_time').first()

