from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/Donor/', null=True, blank=True)

    bloodgroup = models.CharField(max_length=10)

    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class BloodDonate(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=30, default="Nothing")
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0, max_length=2)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def clean(self):
        if self.age > 100:
            raise ValidationError("Age cannot be more than 100.")

    def __str__(self):
        return self.donor
