# Generated by Django 3.1.7 on 2021-03-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopHeadlines', '0002_auto_20210301_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='topheadline_detail',
            name='source',
            field=models.CharField(default='not found', max_length=100),
            preserve_default=False,
        ),
    ]
