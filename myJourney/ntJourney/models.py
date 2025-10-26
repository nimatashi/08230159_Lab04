# Defines database models for Learning Journey and About Me.
from django.db import models

# Model for learning milestones
class LearningStep(models.Model):
    step_no = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()  # editable in Admin

    def str(self):
        return self.title


# Model for personal details
class AboutMe(models.Model):
    name = models.CharField(max_length=100)              # User’s name
    description = models.TextField()                     # Short bio or background
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def str(self):
        return self.name       # Display name in admin panel