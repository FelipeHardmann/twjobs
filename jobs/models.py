from django.db import models


class JobType(models.TextChoices):
    FULL_TIME = "FULL_TIME", "Full Time"
    PART_TIME = "PART_TIME", "Part Time"
    FREELANCE = "FREELANCE", "Freelance"
    INTERSHIP = "INTERSHIP", "Intership"


class JobLevel(models.TextChoices):
    JUNIOR = "JUNIOR", "Junior"
    MIDDLE = "MIDDLE", "Middle"
    SENIOR = "SENIOR", "Senior"


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    job_level = models.CharField(max_length=20, choices=JobLevel.choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    skills = models.ManyToManyField("skills.Skills", related_name='jobs')

    def __str__(self) -> str:
        return self.title
