from django.db import models

# Create your models here.
# 할 일 목록을 위한 모델을 정의
class Todo(models.Model):
    # 할 일을 어떤 데이터 타입으로 저장할 건지 정의
    work = models.CharField(max_length=100)       # CharFiled는 최대 길이 지정 가능
    # work = models.TextField()       # TextFiled는 문자열 길이 제한이 거의 없음
    
    # 완료 여부 저장
    is_completed = models.BooleanField(default=False)
    
    # 언제 만들었는지 저장
        # 날짜만 저장
        # models.DateField
        # 시간만 저장
        # models.TimeField
        # 날짜 + 시간 저장
        # models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.work