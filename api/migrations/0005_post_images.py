# Generated by Django 5.0.2 on 2024-02-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_creator_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Images',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
