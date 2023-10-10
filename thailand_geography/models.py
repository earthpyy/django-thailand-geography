from django.db import models


class Province(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name_en = models.CharField(max_length=100)
    name_th = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)


class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')
    name_en = models.CharField(max_length=100)
    name_th = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)


class Subdistrict(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='subdistricts')
    name_en = models.CharField(max_length=100)
    name_th = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)
