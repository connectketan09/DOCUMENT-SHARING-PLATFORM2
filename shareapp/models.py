from django.db import models
import uuid

class Document(models.Model):

    vault_id = models.UUIDField(default=uuid.uuid4, editable=False)

    file = models.FileField(upload_to='uploads/')

    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    expires_at = models.DateTimeField()

    def __str__(self):
        return str(self.vault_id)