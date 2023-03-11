# Generated by Django 4.1.7 on 2023-03-11 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_rename_establishments_form_establishments'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_history', to='form.form', verbose_name='Мои запросы')),
            ],
            options={
                'verbose_name': 'Мой запрос',
                'verbose_name_plural': 'Мои запросы',
            },
        ),
    ]
