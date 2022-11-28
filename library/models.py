from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.title)      

    class Meta:
        db_table = "books"

class Author(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.OneToOneField("ContactInformation", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (self.name)

    class Meta:
        db_table = "author"

class ContactInformation(models.Model):
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return (self.phone)

    class Meta:
        db_table = "author_contact_information"


class List(models.Model):
    title = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.title