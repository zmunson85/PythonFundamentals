# Generated by Django 2.2.4 on 2020-12-15 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthorApp', '0003_auto_20201214_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='books',
            new_name='book',
        ),
    ]
