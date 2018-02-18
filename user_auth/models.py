from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=20)
    permission = models.SmallIntegerField()

    class Meta:
        db_table = 'roles'
        verbose_name = '用户角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Info(models.Model):
    user = models.OneToOneField(User, related_name='info')
    name = models.CharField(max_length=88, verbose_name='姓名')
    role = models.ForeignKey(Role, default=1, related_name='role_info', verbose_name='角色')
    temp_role = models.ForeignKey(Role, related_name='temp_role_info', null=True, blank=True, verbose_name='临时角色')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    email = models.CharField(max_length=255, verbose_name='邮箱')
    sex = models.SmallIntegerField(choices=((0, '女'), (1, '男'), (2, '不明')), verbose_name='性别')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='居住地')
    company = models.CharField(max_length=255, null=True, blank=True, verbose_name='就职公司')
    college = models.CharField(max_length=80, null=True, blank=True, verbose_name='毕业院校')
    avatar = models.CharField(max_length=255, blank=True, verbose_name='头像', default='default')

    class Meta:
        db_table = 'infos'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
