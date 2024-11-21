from django.db import models

class Bus(models.Model):
    plate_number = models.CharField(max_length=15, unique=True)
    capacity = models.IntegerField()
    route = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.plate_number} - {self.route}"

class BusSchedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="schedules")
    stop = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return f"{self.bus.plate_number} - {self.stop} at {self.time}"
