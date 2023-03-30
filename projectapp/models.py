from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False) #이미지
    title = models.CharField(max_length=20, null=False) #제목
    description = models.CharField(max_length=200, null=True) #프로젝트 설명

    created_at = models.DateTimeField(auto_now=True) #언제 만들어졌는지

    # 게시물 작성 카테고리의 프로젝트명 설정
    def __str__(self):
        return f'{self.pk} : {self.title}' # 출력형식 {게시판 번호 : 게시판 이름}
