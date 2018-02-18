import re

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'tags'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='category_posts')
    tags = models.ManyToManyField(Tag, related_name='tag_posts')
    excerpt = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, related_name='author_posts')
    cover_image = models.CharField(max_length=255)
    view_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    thanks = models.IntegerField(default=0)

    class Meta:
        db_table = 'posts'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s> 发表文章《%s...》' % (self.author, self.title[:23])

    def get_relative_time(self):
        t1 = timezone.now()
        t2 = self.created_time
        years = t1.year - t2.year
        if years > 0:
            return '%d年前' % years
        months = t1.month - t2.month
        if months > 0:
            if months == 6:
                return '半年前'
            return '%d月前' % months
        days = t1.day - t2.day
        if days > 0:
            if days == 15:
                return '半个月前'
            if days == 1:
                return '昨天'
            return '%d天前' % days
        hours = t1.hour - t2.hour
        if hours > 0:
            if hours < 10:
                return '数小时前'
            return '%d小时前' % hours
        minutes = t1.minute - t2.minute
        if minutes > 0:
            if minutes == 12:
                return '半小时前'
            if minutes < 12:
                return '数分钟前'
            return '%d分钟前' % minutes
        return '刚刚'

    def short_title(self):
        return self.title[:14] + ' ...' if len(self.title) > 14 else self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'post_id': self.pk})

    def to_button(self):
        ms = re.findall(r'.*?(&&#&&url=(.*?)&text=(.*?)&&#&&).*?', self.body, re.DOTALL)
        for ole_text, url, text in ms:
            new_text = '<a class="btn btn-primary btn-lg" href="%s" ' \
                       'role="button" style="margin:20px 25px">%s</a>' % (url, text)
            self.body = self.body.replace(ole_text, new_text)

    def save(self, *args, **kwargs):
        self.to_button()
        if self.excerpt is None:
            if len(self.body) < 200:
                self.excerpt = self.body
            else:
                self.excerpt = self.body[:200] + ' ...'
        super(Post, self).save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='category_notes')
    tags = models.ManyToManyField(Tag, related_name='tag_notes')
    view_count = models.IntegerField(default=0)
    status = models.CharField(max_length=16, choices=(
        ('正常', '正常'),
        ('代办', '代办'),
        ('正在处理', '正在处理'),
        ('已完成', '已完成'),
        ('已过期', '已过期'),
    ))

    class Meta:
        db_table = 'notes'
        ordering = ['-created_time']
        verbose_name = '个人笔记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title[:23]


class FriendLink(models.Model):
    name = models.CharField(max_length=88)
    url = models.URLField()

    class Meta:
        db_table = 'friendlinks'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + self.url[:20]


class Contact(models.Model):
    name = models.CharField(max_length=20)
    site = models.URLField(help_text='站点主页')
    img = models.URLField(help_text='站点logo图地址')

    class Meta:
        db_table = 'contacts'
        verbose_name = '社交网站'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='author_comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    praises = models.IntegerField(default=0, help_text='点赞数')
    post = models.ForeignKey(Post, related_name='post_comments')

    class Meta:
        db_table = 'comments'
        verbose_name = '博文评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "<comment %s>" % self.body[:20]
