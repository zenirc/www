from django.db import models
from semantic_version import django_fields as semver_fields


class Service(models.Model):
    author = models.ForeignKey('core.Author')
    name = models.TextField()
    description = models.TextField()
    homepage = models.URLField()


class Author(models.Model):
    name = models.TextField()


class Version(models.Model):
    service = models.ForeignKey('core.Service')
    number = semver_fields.VersionField()
    api_version = models.TextField()
