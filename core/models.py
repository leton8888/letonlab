from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Category(models.Model):
# 	name = models.CharField(u'Name', max_length=50)

# 	def __unicode__(self):
# 		return self.name
# class QRContent(models.Model):
# 	tittle = models.CharField(u'Title', max_length=50)
# 	ss_string = models.TextField(u'SSString')
# 	category = models.ForeignKey('Category', blank=True, null=True)
# 	def __unicode__(self):
# 		return self.tittle


class NavBar(models.Model):
	name = models.CharField(max_length=50, default='nav1')
	tittle = models.CharField(max_length=50, default='tittle')
	def __unicode__(self):
		return self.tittle

class SideBar(models.Model):
	name = models.CharField(max_length=50, default='item1_name')
	tittle = models.CharField(max_length=50, default='item1_tittle')
	navbar = models.ForeignKey(NavBar)
	def __unicode__(self):
		return self.tittle

class Article(models.Model):
	sidebar = models.ForeignKey(SideBar)
	sidebar_name = models.CharField(max_length=50, default='SS1')
	tittle = models.CharField(max_length=50, default='Shadowsocket')
	descript = models.TextField()

	#Shaodowsocks info
	server  = models.CharField(max_length=50, default='127.0.0.1')
	server_port = models.CharField(max_length=50, default='1117')
	password = models.CharField(max_length=50, default='*******')
	#rc4-md5
	method = models.CharField(max_length=50, default='rc4-md5')
	#ss or string
	qr_type = models.CharField(max_length=50, default='ss')