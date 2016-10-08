from __future__ import unicode_literals
from django.db import models


class Participant(models.Model):
    p_id = models.CharField(max_length=30)
    p_name = models.CharField(max_length=100)
    p_alive = models.BooleanField(default=True)
    p_key = models.IntegerField(default=1)
    p_count = models.IntegerField(default=0)
    p_class = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    sum_score = models.IntegerField(default=0)

    class Meta:
        unique_together = ('p_id', 'p_name')

    primary = ('p_id', 'p_name')

    def __unicode__(self):
        return self.p_name


class DataBank1(models.Model):
    q_class = models.IntegerField()
    q_id = models.IntegerField()
    answer = models.CharField(max_length=1)
    content = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    class Meta:
        unique_together = ('q_id', 'q_class')

    primary = ('q_id', 'q_class')

    def __unicode__(self):
        return self.content


class DataBank2(models.Model):
    q_class = models.IntegerField()
    q_id = models.IntegerField()
    answer = models.CharField(max_length=1)
    content = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    class Meta:
        unique_together = ('q_id', 'q_class')

    primary = ('q_id', 'q_class')

    def __unicode__(self):
        return self.content


class DataBank3(models.Model):
    q_class = models.IntegerField()
    q_id = models.IntegerField()
    answer = models.CharField(max_length=1)
    content = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    class Meta:
        unique_together = ('q_id', 'q_class')

    primary = ('q_id', 'q_class')

    def __unicode__(self):
        return self.content
