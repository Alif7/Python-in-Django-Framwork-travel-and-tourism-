# Generated by Django 2.1.3 on 2019-02-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_com'),
    ]

    operations = [
        migrations.CreateModel(
            name='tegory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='com',
            name='post',
        ),
        migrations.DeleteModel(
            name='com',
        ),
    ]
