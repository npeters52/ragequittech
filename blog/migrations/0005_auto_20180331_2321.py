# Generated by Django 2.0.3 on 2018-04-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170617_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]