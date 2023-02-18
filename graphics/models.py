from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)
    area = models.ForeignKey("Area", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Area(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title    

    class Meta:
        ordering = ["title"]


class Direction(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title    

    class Meta:
        ordering = ["title"]


class Budget(models.Model):
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    area = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(default=0)
    direction = models.ForeignKey('Direction', on_delete=models.CASCADE)
    country_budget = models.IntegerField(default=0)
    city_budget = models.IntegerField(default=0)
    grants = models.IntegerField(default=0)
    grants_budget = models.IntegerField(default=0)
    young_people = models.IntegerField(default=0)
    public_associations = models.IntegerField(default=0)

    class Meta:
        ordering = ["region"]

    def save(self, *args, **kwargs):
        self.area = str(self.region.area)
        return super(Budget, self).save(*args, **kwargs)
