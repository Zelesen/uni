# Generated by Django 3.2.25 on 2024-09-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockmanya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
