# Generated by Django 3.2.7 on 2021-09-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sport', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ApiModel',
        ),
    ]
