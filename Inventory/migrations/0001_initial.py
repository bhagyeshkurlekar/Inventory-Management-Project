# Generated by Django 2.2.3 on 2019-07-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('order', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=50)),
                ('reference_order', models.CharField(max_length=50)),
                ('products', models.CharField(max_length=50)),
            ],
        ),
    ]