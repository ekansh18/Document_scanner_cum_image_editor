# Generated by Django 3.2.3 on 2021-05-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_upload_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
