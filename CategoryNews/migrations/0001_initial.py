# Generated by Django 3.1.7 on 2021-03-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCat',
            fields=[
                ('id', models.DecimalField(decimal_places=2, max_digits=5, primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('UrlToImage', models.ImageField(blank=True, max_length=1000, null=True, upload_to='')),
                ('PublishedAt', models.DateField()),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]