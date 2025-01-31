from django.db import models
from django.utils import timezone

class _BaseModel(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(archived__isnull=True)
            .filter(archived=None)
        )


class BaseModelQuerySet(models.QuerySet):
    pass


BaseModelManager = _BaseModel.from_queryset(BaseModelQuerySet)


class BaseModel(models.Model):
    archived = models.DateTimeField(blank=True, null=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = BaseModelManager()
    super_objects = models.Manager()

    def archive(self):
        self.archived = timezone.now()
        super().save()


    class Meta:
        abstract = True
        ordering = ["-last_modified"]