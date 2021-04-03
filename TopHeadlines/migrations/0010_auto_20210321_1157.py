# Generated by Django 3.1.7 on 2021-03-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopHeadlines', '0009_auto_20210310_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topheadline_detail',
            name='UrlToImage',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='author',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='content',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='source',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='topheadline_detail',
            name='url',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
    ]