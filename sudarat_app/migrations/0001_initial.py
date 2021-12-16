# Generated by Django 3.2.7 on 2021-10-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sudarat_tb_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_studentId', models.CharField(max_length=200)),
                ('member_firstname', models.CharField(max_length=200)),
                ('member_lastname', models.CharField(max_length=200)),
                ('member_detail', models.TextField()),
                ('member_image', models.ImageField(default='', upload_to='photo')),
            ],
        ),
    ]