# Generated by Django 2.2.10 on 2020-03-28 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200328_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='image_l',
            field=models.ImageField(max_length=1000, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_l',
            field=models.ImageField(max_length=1000, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='service',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='core.ServiceGroup', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.CharField(blank=True, max_length=255, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='service',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Unit', verbose_name='Еденица измерения'),
        ),
    ]