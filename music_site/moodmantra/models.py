from django.db import models

class signup(models.Model):
    Name = models.CharField(max_length=30)
    Email =  models.EmailField()
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Email