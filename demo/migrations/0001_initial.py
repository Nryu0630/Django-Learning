# Generated by Django 5.0.3 on 2024-03-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='姓名')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
            ],
        ),
    ]
