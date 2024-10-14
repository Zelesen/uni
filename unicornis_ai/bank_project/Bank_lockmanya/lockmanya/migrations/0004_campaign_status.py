# Generated by Django 5.1.1 on 2024-10-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockmanya', '0003_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('running', 'Running'), ('closed', 'Closed')], default='created', max_length=20),
        ),
    ]
