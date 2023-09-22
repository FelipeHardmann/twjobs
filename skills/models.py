from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def to_json(self):
        return {
            "name": self.name
        }
