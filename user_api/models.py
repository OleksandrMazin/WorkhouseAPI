from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self) -> (str):
        return self.name


class Category(models.Model):
    cat = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.cat