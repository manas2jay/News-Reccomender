# Generated by Django 3.1.7 on 2021-04-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storenews', '0002_auto_20210321_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_news',
            name='user',
            field=models.TextField(),
        ),
    ]