# Generated by Django 4.1.5 on 2023-01-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgmobileshopapp', '0002_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default=1, upload_to='brandlogo'),
            preserve_default=False,
        ),
    ]
