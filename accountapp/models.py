from django.db import models

# Create your models here.

class HelloWorld(models.Model): #ctrl+b 누르면 해당 자식으로 이동
    text = models.CharField(max_length=255, null=False) #null -> DB에 저장할 때 text가 없어도 되는지(Flase가 있어야된다라고 명시하는 것)