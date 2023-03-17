from django.db import models

# Create your models here.

# Lista de capitura de email
class NewslettersUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

# Conteúdo da Newsletter informativa
class Newsletter(models.Model):

    EMAIL_STATUS_CHOICES= (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body=models.TextField(blank=True, null=True)
    email = models.ManyToManyField(NewslettersUser)  # esta relacionado com a nossa acima
    created = models.DateTimeField(auto_now_add=True)

    status=models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)

    def __str__(self):
        return self.name

    # Ordenando as entradas por onde de chegada
    class Meta:
        ordering = ('-created',)
