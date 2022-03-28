from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone

# from apps.rbac.models import Role



class User(AbstractUser):
    user_id = models.BigIntegerField(verbose_name='用户ID', unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    name = models.CharField(max_length=32, verbose_name='姓名')
    job_number = models.CharField(max_length=32, verbose_name='工号', null=True, blank=True)
    position = models.CharField(max_length=64, null=True, verbose_name='职位信息', blank=True)
    hire_date = models.DateTimeField(verbose_name='入职时间', null=True)
    # avatar = models.URLField(verbose_name='用户头像', null=True, blank=True)
    # sex = models.CharField(max_length=8, verbose_name='性别', choices=(('man', '男'), ('women', '女')), default='man')
    # roles = models.ManyToManyField(Role, verbose_name='角色', blank=True)
    # department = models.CharField(max_length=128, verbose_name='部门', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name



class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(verbose_name='权限名称', max_length=32, unique=True)
    path = models.CharField(verbose_name='含正则的URL', blank=True, max_length=128)
    method = models.CharField(verbose_name='方法', max_length=16, default='GET')
    pid = models.ForeignKey('self', verbose_name='上级权限', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(verbose_name='角色名称', max_length=32, unique=True)
    permissions = models.ManyToManyField('Permission', verbose_name='权限', blank=True)
    #menus = models.ManyToManyField('Menu', verbose_name='菜单', blank=True)
    desc = models.CharField(verbose_name='描述', max_length=50, blank=True)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name
