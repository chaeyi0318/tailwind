from django.db import models

# Create your models here.
                # 상위 클래스를 상속
class Article(models.Model):
    title = models.CharField(max_length=10)     # models의 클래스 CharField
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)        # 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장
    updated_at = models.DateTimeField(auto_now=True)        # 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장