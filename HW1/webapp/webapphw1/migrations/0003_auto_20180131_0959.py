# Generated by Django 2.0.1 on 2018-01-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapphw1', '0002_auto_20180130_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zodiac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
