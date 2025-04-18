from django.db import models

class gamelock(models.Model):
    """
    Model representing a game lock.
    """
    game_time = models.DateTimeField()
    limited_timed_event = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Game Lock: {self.game_time} - {self.limited_timed_event}"