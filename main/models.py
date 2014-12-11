from adminsortable.models import Sortable
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.db.models import TextField


class Element(Sortable):
    class meta(Sortable.Meta):
        pass

    title = models.CharField(max_length=255)
    description = RichTextField()

    def __unicode__(self):
        return self.title

class Example(Sortable):
    class meta(Sortable.Meta):
        pass

    element = models.ForeignKey(Element)
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    code = TextField()

    def __unicode__(self):
        return self.element.title + " - " + self.title
