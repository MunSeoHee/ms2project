# Generated by Django 3.0.7 on 2020-08-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200822_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.TextField(),
        ),
    ]
