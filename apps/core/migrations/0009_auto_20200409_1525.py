# Generated by Django 2.2.10 on 2020-04-09 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200409_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=0, max_length=255, verbose_name='Имя клиента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Service', verbose_name='Оказанная услуга'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Комментарий'),
        ),
    ]