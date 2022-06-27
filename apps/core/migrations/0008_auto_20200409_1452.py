# Generated by Django 2.2.10 on 2020-04-09 11:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200328_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.TextField()),
                ('checked', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-datetime'],
            },
        ),
        migrations.AlterModelOptions(
            name='servicegroup',
            options={'ordering': ['index']},
        ),
        migrations.CreateModel(
            name='CommentImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_l', models.ImageField(max_length=1000, null=True, upload_to='', verbose_name='Картинка')),
                ('image_l_size', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_l_url', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_m', models.ImageField(blank=True, editable=False, null=True, upload_to='')),
                ('image_m_size', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_m_url', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_s', models.ImageField(blank=True, editable=False, null=True, upload_to='')),
                ('image_s_size', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_s_url', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_xs', models.ImageField(blank=True, editable=False, null=True, upload_to='')),
                ('image_xs_size', models.CharField(blank=True, editable=False, max_length=1000)),
                ('image_xs_url', models.CharField(blank=True, editable=False, max_length=1000)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.Comment', verbose_name='Фото')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]