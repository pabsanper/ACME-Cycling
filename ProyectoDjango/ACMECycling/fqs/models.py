from django.db import models

class PreguntasFrecuentes(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta
