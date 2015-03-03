# codeing=utf-8

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
    status = models.IntegerField(_('status'), db_index=True, choices=STATUS_CHOICES, default=DRAFT)
    start_publication = models.DateTimeField('start publication', db_index=True, blank=True,
                                             null=True, help_text='Start date of publication.')
    end_publication = models.DateTimeField('end publication', db_index=True, blank=True, null=True,
                                           help_text='End date of publication.')
    creation_date = models.DateTimeField('creation date', db_index=True, default=timezone.now,
                                         help_text="Used to build the entry's URL.")
    last_update = models.DateTimeField('last update', default=timezone.now)

