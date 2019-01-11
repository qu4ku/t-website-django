# Generated by Django 2.1.4 on 2019-01-04 05:49

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190104_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image_alt',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=core.models.default_start_time),
        ),
    ]