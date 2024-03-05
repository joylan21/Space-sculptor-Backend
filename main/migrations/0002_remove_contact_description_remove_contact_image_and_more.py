# Generated by Django 4.1.7 on 2024-03-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]