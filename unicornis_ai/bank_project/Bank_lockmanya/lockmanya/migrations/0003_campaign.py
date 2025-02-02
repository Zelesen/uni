# Generated by Django 5.1.1 on 2024-10-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockmanya', '0002_auto_20240930_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=255)),
                ('audience', models.CharField(max_length=255)),
                ('campaign_type', models.CharField(max_length=50)),
                ('campaign_goal', models.CharField(max_length=50)),
                ('advertisement_type', models.CharField(max_length=50)),
                ('advertisement_text', models.TextField()),
                ('ad_file', models.FileField(upload_to='ads/')),
            ],
        ),
    ]
