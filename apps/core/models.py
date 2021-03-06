from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from django_cleanup import cleanup
from project import settings
from PIL import Image
import io
import os
import shutil
import unidecode


def imageFilename(self, filename):
    ext = filename.split('.')[-1]
    app_name = self._meta.app_label
    model_name = self._meta.model_name

    name_attrs = ['id' + str(self.pk)]
    name = ''
    parent = self
    models_attrs = ['slug', 'code']
    while parent != None:
        for attr in models_attrs:
            if hasattr(parent, attr):
                if getattr(parent, attr) != None:
                    name_attrs.insert(0, str(getattr(parent, attr)))
        if hasattr(parent, 'brand'):
            name_attrs.insert(0, str(parent.brand.slug))
        if hasattr(parent, 'parent'):
            parent = parent.parent
        else:
            parent = None
    name = '_'.join(name_attrs)
    name = slugify(str(name))

    # APP NAME PATH
    app_name_path = settings.MEDIA_ROOT + app_name + '/'
    app_name_dir = os.path.isdir(app_name_path)
    if app_name_dir == False:
        os.mkdir(app_name_path)

    # MODEL NAME PATH
    model_name_path = settings.MEDIA_ROOT + app_name + '/' + model_name + '/'
    model_name_dir = os.path.isdir(model_name_path)
    if model_name_dir == False:
        os.mkdir(model_name_path)

    filename = '.'.join([name, ext])
    path = '/'.join([app_name, model_name, filename])

    return path


# IMAGES
@cleanup.ignore
class Images(models.Model):
    # LARGE
    image_l = models.ImageField(upload_to=imageFilename, max_length=1000, blank=False, null=True, editable=True)
    image_l_size = models.CharField(max_length=1000, blank=True, editable=False)
    image_l_url = models.CharField(max_length=1000, blank=True, editable=False)
    # MEDIUM
    image_m = models.ImageField(blank=True, null=True, editable=False)
    image_m_size = models.CharField(max_length=1000, blank=True, editable=False)
    image_m_url = models.CharField(max_length=1000, blank=True, editable=False)
    # SMALL
    image_s = models.ImageField(blank=True, null=True, editable=False)
    image_s_size = models.CharField(max_length=1000, blank=True, editable=False)
    image_s_url = models.CharField(max_length=1000, blank=True, editable=False)
    # EXTRA SMALL
    image_xs = models.ImageField(blank=True, null=True, editable=False)
    image_xs_size = models.CharField(max_length=1000, blank=True, editable=False)
    image_xs_url = models.CharField(max_length=1000, blank=True, editable=False)
    # REGENERATE
    regen = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True

    def save(self):
        def get_filename(f_name, f_ext, key):
            if key == 'l':
                return f_name + '.' + f_ext
            return f_name + '_' + key + '.' + f_ext

        if self.image_l.url != '/media/' + self.image_l_url or self.regen == True:
            super(Images, self).save()
            sizes = (
                ('l', 1600),
                ('m', 960),
                ('s', 480),
                ('xs', 128),
            )

            file_name = str(imageFilename(self, self.image_l.name))
            file_name = str(file_name).split('.')
            ext = file_name[-1]
            name = file_name[0]

            # CREATE IMAGES
            for key, value in sizes:
                img = Image.open(self.image_l.file)

                filename = get_filename(name, ext, key)
                attr = getattr(self, 'image_' + key)
                setattr(attr, 'name', filename)
                img.thumbnail((value, value), Image.ANTIALIAS)
                setattr(self, 'image_' + key + '_size', str(img.size[0]) + 'x' + str(img.size[1]))
                setattr(self, 'image_' + key + '_url', filename)
                img.save(settings.MEDIA_ROOT + filename, quality=100)
            img.close()
        self.regen = False
        super(Images, self).save()

    def delete(self):
        print('DLETE')
        for key in ['l', 'm', 's', 'xs']:
            path = getattr(self, 'image_' + key + '_url')
            try:
                os.remove(settings.MEDIA_ROOT + path)
            except:
                pass
        super(Images, self).delete()


class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name="?????????????? ????????????????")

    def __str__(self):
        return self.name


class MainService(Images):
    name = models.CharField(max_length=255, verbose_name="??????????????????")
    slug = models.CharField(max_length=255, verbose_name="??????????????????????????", blank=True)
    index = models.PositiveIntegerField(default=0, verbose_name="?????????? ?? ?????????????? ??????????????????????", blank=True)

    class Meta:
        ordering = ['index']

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(str(unidecode.unidecode(self.name)))
        super(MainService, self).save()


class PriceTable(models.Model):
    CHOICES = (
        ('??????.', '??????.'),
        ('??????. / ????.', '??????. / ????.'),
        ('??????. / ??????', '??????. / ??????'),
    )
    name = models.CharField(max_length=255, verbose_name="???????????????? ????????????")
    price = models.PositiveIntegerField(default=0, verbose_name="????????")
    unit = models.CharField(max_length=24, choices=CHOICES, verbose_name="?????????????? ????????????????")
    order = models.PositiveIntegerField(default=0, verbose_name="??????????????")
    helptext = models.CharField(max_length=500, verbose_name="??????????????????", blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = "???????? ???? ????????????"
        verbose_name_plural = "???????????? ??????"

    def __str__(self):
        return self.name


class ServiceGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="???????????????? ????????????")
    title = models.CharField(max_length=255, verbose_name="??????????????????")
    subtitle = models.CharField(max_length=255, verbose_name="??????????????????????")
    slug = models.CharField(max_length=255, verbose_name="??????????????????????????", blank=True)
    index = models.PositiveIntegerField(default=0, verbose_name="?????????? ?? ?????????????? ??????????????????????", blank=True)
    counter = models.BooleanField(default=False, verbose_name="?????????????? ??????????????", blank=True)

    class Meta:
        ordering = ['index']

    def __str__(self):
        return f"#{self.index} {self.name}"

    def save(self):
        self.slug = slugify(str(unidecode.unidecode(self.name)))
        super(ServiceGroup, self).save()


class Service(Images):
    parent = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, related_name='service', verbose_name="????????????")
    name = models.CharField(max_length=255, verbose_name="??????????????????")
    subtitle = models.CharField(max_length=255, verbose_name="??????????????????????")
    slug = models.CharField(max_length=255, verbose_name="??????????????????????????", blank=True)
    price = models.PositiveIntegerField(default=0, verbose_name="????????", blank=True)
    index = models.PositiveIntegerField(default=0, verbose_name="?????????? ?? ?????????????? ??????????????????????", blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="?????????????? ??????????????????", blank=True, null=True)
    blank = models.BooleanField(default=False, blank=True)

    def save(self):
        self.slug = slugify(str(unidecode.unidecode(self.name)))
        super(Service, self).save()

    def __str__(self):
        return self.name


class Comment(models.Model):
    stars = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    name = models.CharField(max_length=255, blank=False, verbose_name="?????? ??????????????")
    phone = models.CharField(max_length=255, blank=False, verbose_name="?????????? ????????????????")
    service = models.ForeignKey(MainService, on_delete=models.CASCADE, verbose_name="?????????????????? ????????????")
    text = models.TextField(verbose_name="??????????????????????")
    checked = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=now, blank=True, editable=False)

    class Meta:
        ordering = ['-datetime']
        verbose_name = '??????????????????????'
        verbose_name_plural = '??????????????????????'

    def __str__(self):
        stars = [
            "????????????", "??????????", "??????????????????", "????????????", "??????????????"
        ]
        return f"{self.datetime.strftime('%H:%M %d/%m/%Y')} | ????????????: {stars[self.stars - 1]} | {self.name} | {self.service.name}"

    def save(self):
        symbols = ['@', 'http', 'https', 'www']
        if not any(ext in self.text for ext in symbols):
            super(Comment, self).save()

    def rating(self):
        stars = []
        for i in range(0, 5):
            if i >= int(self.stars):
                stars.append(1)
            else:
                stars.append(0)
        return stars


class CommentImages(Images):
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="????????", related_name='images')
