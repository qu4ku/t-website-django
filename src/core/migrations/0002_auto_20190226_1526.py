# Generated by Django 2.1.5 on 2019-02-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seo_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='seo_title',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
