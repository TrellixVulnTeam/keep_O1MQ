from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, verbose_name='主键')
    activity_id = models.CharField(max_length=128, verbose_name='活动ID')
    seq = models.IntegerField(verbose_name='序号，步长100')
    question_type = models.SmallIntegerField(verbose_name='问题类型 1 大事件题目 2 每日竞猜题目')
    show_type = models.SmallIntegerField(verbose_name='题目形式 1 文字 2 图片 3 视频')
    content = models.CharField(max_length=512, verbose_name='问题 json 题目内容 选项 url等')
    answer_explain = models.CharField(max_length=512, verbose_name='答案解释 含讲解视频等')
    answer = models.CharField(max_length=1, verbose_name='问题的答案 A B C D等')
    enable = models.SmallIntegerField(verbose_name='0 未启用 1 未启用')
    show_day = models.DateField(verbose_name='展示日期')
    close_time = models.DateTimeField(verbose_name='答题截止日期')
    answer_time = models.DateTimeField(verbose_name='答案公布时间')
    answer_status = models.SmallIntegerField(verbose_name='答案公布状态 0 未公布 1 已公布')
    extra = models.CharField(max_length=512, verbose_name='json 扩展字段')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

