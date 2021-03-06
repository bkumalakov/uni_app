# Generated by Django 3.2.6 on 2022-05-20 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(help_text='Номер распоряжения')),
                ('order_date', models.DateField(help_text='Дата распоряжения')),
                ('order_heading', models.CharField(help_text='Заголовок распоряжения', max_length=150)),
                ('order_body', models.CharField(help_text='Тело распоряжения', max_length=2000)),
                ('order_signed_doc', models.FileField(blank=True, upload_to='Подписанный документ')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
