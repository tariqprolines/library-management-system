# Generated by Django 2.2.3 on 2019-07-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsmanage', '0002_auto_20190713_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]