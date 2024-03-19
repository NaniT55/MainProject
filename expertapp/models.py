from django.db import models

# Create your models here.
class Response(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    query_id = models.IntegerField()
    response_text = models.TextField()

    class Meta:
        db_table = 'Respones_expert'


