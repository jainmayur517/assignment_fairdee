# Generated by Django 2.2.7 on 2021-04-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210410_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertwitx',
            name='url_p',
            field=models.TextField(default=-1, max_length=500),
            preserve_default=False,
        ),
    ]
