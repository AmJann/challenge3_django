from django.db import models

class User(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name


class Score (models.Model):
    score = models.IntegerField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    game_code = models.ForeignKey("game.Player", on_delete=models.CASCADE)
