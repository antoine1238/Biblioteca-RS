# Generated by Django 3.2.8 on 2021-11-06 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_synopsis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autor',
            new_name='author',
        ),
    ]
