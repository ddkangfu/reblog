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


class Category(models.Model):
    title = models.CharField(u"标题", max_length=255)
    slug = models.SlugField('slug', unique=True, max_length=255, help_text="Used to build the category's URL.")
    description = models.TextField('description', blank=True)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, verbose_name='parent category')
    objects = TreeManager()


class TagsEntry(models.Model):
    tags = TagField(_('tags'))

    @property
    def tags_list(self):
        """
        Return iterable list of tags.
        """
        return parse_tag_input(self.tags)

    class Meta:
        abstract = True
