from django.db import models
from django.utils import timezone

class Dojo(models.Model):
    name = models.CharField()
    city = models.CharField()
    state = models.CharField()
    desc=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.city}"
    

class Ninja(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    dojo = models.ForeignKey(Dojo , related_name="ninjas" , on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"name:{self.first_name} {self.last_name} (Dojo: {self.dojo.name})"
      
