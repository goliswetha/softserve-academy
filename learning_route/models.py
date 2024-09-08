from django.db import models
from django.core.validators import MinValueValidator
from skill.models import SkillLevel
from learning_resource.models import LearningResource

# id: int
# LearningRoute: LearningRoute
# learning_resource: LearningResource
# completed: bool
# time_spent: int
class LearningRouteResource(models.Model):
    LearningRoute = models.ForeignKey('LearningRoute', on_delete=models.CASCADE)
    learning_resource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], blank=True)


# id: int
# skillLevel: SkillLevel
# duration: int
# learning_resources: learningRouteResource[]
# actual_resource_index: int
# completed: bool
class LearningRoute(models.Model):
    skillLevel = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    learning_resources = models.ManyToManyField(LearningResource, through='LearningRouteResource')
    actual_resource_index = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], blank=True)

    def __str__(self):
        return self.skillLevel.skill.name + ' - ' + str(self.skillLevel.level)