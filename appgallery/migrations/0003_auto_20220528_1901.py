# Generated by Django 3.2.10 on 2022-05-28 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgallery', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='location_id',
            new_name='location',
        ),
    ]
