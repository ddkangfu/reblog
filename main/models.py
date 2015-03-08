# coding=utf-8

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from django.db import models
from django.utils import timezone


DRAFT = 0
HIDDEN = 1
PUBLISHED = 2


class Post(models.Model):
    STATUS_CHOICES = ((DRAFT, 'draft'),
                     (HIDDEN, 'hidden'),
                     (PUBLISHED, 'published'))
    title = models.CharField(u"标题", max_length=60)
    slug = models.SlugField('slug', max_length=255,
                            unique_for_date='creation_date', help_text="Used to build the entry's URL.")
    status = models.IntegerField('status', db_index=True, choices=STATUS_CHOICES, default=DRAFT)
    start_publication = models.DateTimeField('start publication', db_index=True, blank=True,
                                             null=True, help_text='Start date of publication.')
    end_publication = models.DateTimeField('end publication', db_index=True, blank=True, null=True,
                                           help_text='End date of publication.')
    creation_date = models.DateTimeField('creation date', db_index=True, auto_now_add=True,
                                         help_text="Used to build the entry's URL.")
    last_update = models.DateTimeField('last update', default=timezone.now)

    @property
    def is_actual(self):
        now = timezone.now()
        if self.start_publication and now < self.start_publication:
            return False

        if self.end_publication and now >= self.end_publication:
            return False
        return True

    @property
    def is_visible(self):
        return self.is_actual and self.status == PUBLISHED

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s: %s' % (self.title, self.get_status_display())

    class Meta:
        ordering = ['-creation_date']


class Category(MPTTModel):
    title = models.CharField(u"标题", max_length=255)
    slug = models.SlugField('slug', unique=True, max_length=255, help_text="Used to build the category's URL.")
    description = models.TextField('description', blank=True)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, verbose_name='parent category')
    objects = TreeManager()


class TagsEntry(models.Model):
    name = models.CharField(u"标签", max_length=255)
    is_deleted = models.BooleanField(u'是否已删除', default=False)

