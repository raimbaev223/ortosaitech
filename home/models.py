from django.db import models

class MainContent(models.Model):
    image = models.ImageField(upload_to="main_img/", verbose_name="Главное фото")
    title = models.CharField(max_length=255, verbose_name="Главный заголовок")


class HomepageBlock(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to="home_img/", verbose_name='Картинка')


class Order(models.Model):
    machine = models.CharField(max_length=255, verbose_name="Модель машинки", null=True, blank=True)
    malfunction = models.CharField(max_length=255, verbose_name="Неисправность", null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    note = models.TextField(max_length=500, verbose_name="Примечание", null=True, blank=True)
    time = models.TimeField(verbose_name='Время', null=True, blank=True)
    summ = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Сумма за ремонт", null=True, blank=True)
    costs = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Расходы на ремонт", null=True, blank=True)
    check = models.BooleanField(default=False, verbose_name="Выполнено")
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.address} {self.phone} {self.machine}"