from datetime import datetime
from django.db import models


class Order(models.Model):
    order_number = models.IntegerField(help_text="Номер распоряжения", verbose_name='Номер')
    order_date = models.DateField(help_text="Дата подпясания распоряжения", verbose_name='Дата')
    order_heading = models.CharField(max_length=150, help_text="Заголовок распоряжения",
                                     verbose_name='Заголовок распоряжения')
    order_body = models.CharField(max_length=2000, help_text="Тело распоряжения")
    order_signed_doc = models.FileField(upload_to='docs/', blank=True, verbose_name='Файл')
    date_created = models.DateTimeField(default=datetime.now, blank=True)                       #object creation date and time
    last_updated = models.DateTimeField(auto_now=True)                                          #date and time of the last object update

    class Meta:
        verbose_name = "Распоряжение"
        verbose_name_plural = "Распоряжения"

    def __str__(self):
        return str(self.order_number) + ' от ' + str(self.order_date)


