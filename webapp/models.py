#-*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=30,blank=True,null=True)
    unit = models.CharField(max_length=15,blank=True,null=True)
    qq =  models.PositiveIntegerField(blank=True,null=True,verbose_name='qq号码')
    dec = models.CharField(max_length=100,blank=True,null=True,verbose_name='个人信息')
    friends = models.ManyToManyField('self')
    def __unicode__(self):
        return self.last_name+self.first_name

class Achievements(models.Model):
    title = models.CharField(max_length=20,verbose_name='成果标题')
    dec =  models.CharField(max_length=100,verbose_name='成果详细介绍')

class Prizes(models.Model):
    GRADE_CHOICES = (
        ('ONE','一等奖'),
        ('TWO','二等奖'),
        ('THREE','三等奖'),
        ('FOUR','特等奖'),
        ('OTHERS','其他'),
    )
    HEIGHT_CHOICES = (
        ('one','世界级'),
        ('two','国家级'),
        ('three','省级'),
        ('four','区级'),
        ('others','其他'),
    )
    matchName =models.CharField(max_length=20,verbose_name='赛名')
    height = models.CharField(max_length=6,choices=HEIGHT_CHOICES)
    grade = models.CharField(max_length=6,choices=GRADE_CHOICES)
    dec = models.CharField(max_length=150)
    def __unicode__(self):
        return self.matchName

class Team(models.Model):
    name = models.CharField(max_length=52)
    abouts = models.CharField(max_length=100,verbose_name='团队介绍',blank=True,null=True)
    achievement = models.ForeignKey(Achievements,blank=True,null=True)
    prize = models.ForeignKey(Prizes,related_name='teamPrize_set',blank=True,null=True)
    def __unicode__(self):
        return self.name

class SupperUser(User):
    team = models.ForeignKey(Team)
    supperDec = models.CharField(max_length=500,verbose_name='技能介绍')
    def __unicode__(self):
        return self.last_name+self.first_name
    class Meta:
        verbose_name_plural = '团队成员'

class Text(models.Model):
    content = models.TextField(max_length=8000)
    date_publish = models.DateTimeField(default=timezone.now)

class Question(Text):
    title = models.CharField(max_length=30,verbose_name='问题标题')
    user = models.ForeignKey(User)

class Blog(Text):
    title = models.CharField(max_length=30,verbose_name='博客标题')
    user = models.ForeignKey(SupperUser)
    def __unicode__(self):
        return self.title

class comment(Text):
    to = models.ForeignKey(User,related_name='beComment_set')
    user = models.ForeignKey(User)

class Fans(models.Model):
    user = models.ForeignKey(User,related_name='care_set')
    god = models.ForeignKey(SupperUser,related_name='fans_set')

class Tweets(Text):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
