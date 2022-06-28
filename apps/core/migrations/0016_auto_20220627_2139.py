# Generated by Django 2.2.10 on 2022-06-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200409_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('unit', models.CharField(max_length=24, verbose_name='Еденица имерения')),
            ],
        ),
        migrations.AlterField(
            model_name='commentimages',
            name='image_m',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='image_m',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_m',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
    ]