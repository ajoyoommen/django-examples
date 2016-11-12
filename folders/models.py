from __future__ import unicode_literals

from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='sub_folders')
    path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = (('name', 'parent'), )

    def __unicode__(self):
        return self.path

    def save(self, *args, **kwargs):
        self.path = self._construct_path()
        super(Folder, self).save(*args, **kwargs)

    def _construct_path(self):
        path = self.name
        parent = self.parent
        while parent:
            path = parent.name + '/' + path
            parent = parent.parent
        return path
