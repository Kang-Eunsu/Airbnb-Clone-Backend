from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)  # 생성된 시간 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)  # 마지막으로 업데이트된 시간 자동으로 저장

    class Meta:  # 장고가 데이터베이스에 저장하지 않도록
        abstract = True
