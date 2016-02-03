from __future__ import unicode_literals

from django.db import models
#from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('dato puclico')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo

'''
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
'''