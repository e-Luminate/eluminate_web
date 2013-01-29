from django.db import models
from participant.models import Participant

DAYS = (
        ("We", "20th Wednesday"),
        ("Tu", "21rs Thursday"),
        ("Fr", "22nd Friday"),
        ("Sa", "23rd Saturday"),
        ("Su", "24th Sunday")
        )

class Event(models.Model):
    name = models.CharField(max_length = 256)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.CharField(max_length=2,
                            choices=DAYS,
                            default=None
                            )
    participant = models.ForeignKey(Participant)
    description = models.TextField()
