# Generated by Django 2.2.3 on 2019-07-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created',
            field=models.CharField(max_length=20),
        ),
    ]
