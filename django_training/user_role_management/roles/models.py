from django.db import models

class Role(models.Model):
    roleName = models.CharField(max_length=100)
    accessModules = models.JSONField(default=list)  # Store access modules as a list of strings
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.roleName
    
    