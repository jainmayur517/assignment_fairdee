# Generated by Django 2.2.7 on 2021-04-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertwitx',
            name='image',
        ),
        migrations.AddField(
            model_name='usertwitx',
            name='user_c',
            field=models.CharField(default=-1.0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertwitx',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
