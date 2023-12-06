from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    body = models.CharField(_("Body"), max_length=50)

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("Todo_detail", kwargs={"pk": self.pk})
