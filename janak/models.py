from django.db import models

class GeneratedEmail(models.Model):
    prompt = models.TextField()
    generated_email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email generated from: {self.prompt[:50]}..."