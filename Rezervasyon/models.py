from django.db import models
from django.contrib.auth.models import User

class Rezervasyon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.PositiveIntegerField()
    reservation_time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.reservation_time}"

