# Generated by Django 3.1.7 on 2021-03-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopHeadlines', '0008_auto_20210302_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topheadline_detail',
            name='UrlToImage',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]