from django.db import models

class Body(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class Result(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class FitnessClass(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class Schedule(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class Trainer(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class Servise(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()


class Form(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)
    body = models.TextField()

    
    def __str__(self):
        return f"{self.first_name}"
    

    class Meta:
        verbose_name = "Mo`yxati"
        verbose_name_plural = ""
        ordering = ("")

