# Generated by Django 3.2.3 on 2021-11-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudarat_app', '0003_remove_sudarat_tb_model_date_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudarat_tb_model',
            name='date_news',
            field=models.DateTimeField(auto_now=True),
        ),
    ]