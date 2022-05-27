from django.db import models


class UserModel(models.Model):
    def __init__(self, email, password):
        self.username = email
        self.password = password

    class Meta:
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)