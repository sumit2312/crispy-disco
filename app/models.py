from django.db import models

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length = 50)
	problemLink = models.URLField(max_length=250)
	explanation = models.TextField()
	programLink = models.URLField(max_length=250)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title

class Comment(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	comment = models.TextField()
	name = models.CharField(max_length=50)

class Request(models.Model):
	problem = models.URLField(max_length=250)
