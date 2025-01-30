from django.core.validators import FileExtensionValidator
from django.db import models


class Task(models.Model):
    name = models.CharField('Название товара', max_length=100)
    manufacturer = models.CharField('Производитель', max_length=100, )
    price = models.IntegerField('Цена')
    square = models.IntegerField('В магазине')

    thumbnail = models.ImageField(
        verbose_name='Превью поста', blank=True,
        upload_to='images/thumbnails/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Orders(models.Model):
    created = models.DateTimeField(verbose_name='Дата', auto_now_add=True, blank=True)
    owner = models.ForeignKey('auth.User', verbose_name='Название', related_name='orders_user',
                              on_delete=models.CASCADE)
    task = models.ForeignKey('Task', verbose_name='Заказы', related_name='orders_task', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created)

    def get_absolute_url(self):
        return "/orders/%s" % self.owner.username
        # return "/orders/%i/" % self.id

    class Meta:
        ordering = ['created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
