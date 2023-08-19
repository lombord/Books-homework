from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    class Meta:
        constraints = models.UniqueConstraint(
            Lower("first_name").desc(),
            Lower("last_name").desc(),
            name="first_last_name_lower_unique",
            violation_error_message=_("Full name must be unique!")),

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        constraints = models.UniqueConstraint(
            Lower("name").desc(),
            name="name_lower_unique",
            violation_error_message=_("Genre name must be unique!")),

    def __str__(self) -> str:
        return self.name


def get_current_year():
    return now().year


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(Author,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name="books")
    published_year = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(get_current_year,
                                      _("Invalid year value!")),])
    genre = models.ForeignKey(Genre,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="books")
    rating = models.DecimalField(max_digits=2, decimal_places=0, validators=[
                                 MaxValueValidator(10),])
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = "-pk",

    def get_absolute_url(self, *, name="book"):
        return reverse(name, kwargs={'slug': self.slug})

    def increase_views(self):
        self.views = models.F('views') + 1
        super().save()
        self.refresh_from_db()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
