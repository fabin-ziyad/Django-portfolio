# Generated by Django 3.2.10 on 2022-07-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0018_contacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='github',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='link',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter',
        ),
        migrations.AddField(
            model_name='contact',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='Messages',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='contact',
            name='Name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='contact',
            name='Subjects',
            field=models.CharField(default='', max_length=250),
        ),
    ]