from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # 객체 사라질 때 프로필도 같이 없어지게
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name ='profile')

    image = models.ImageField(upload_to='profile/', null=True) # 없어도 된다
    nickname = models.charField(max_length=20, unique=True, null=True) # 중복X
    message = models.CharFiedl(max_length=100, null=True)
