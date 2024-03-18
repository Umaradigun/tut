from django.db import models

# Create your models here.
class (models.Model):


    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

        title = models.CharField(max_length= 100),
        authors_name= models.CharField(max_length=50),
        ratings= models.IntegerField(default=True),

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
