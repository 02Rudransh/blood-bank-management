# from django.db import models
# from patient import models as pmodels
# from donor import models as dmodels


# class Stock(models.Model):
#     bloodgroup = models.CharField(max_length=10)
#     unit = models.PositiveIntegerField(max_length=2)

#     def __str__(self):
#         return self.bloodgroup


# class BloodRequest(models.Model):
#     request_by_patient = models.ForeignKey(
#         pmodels.Patient, null=True, on_delete=models.CASCADE)
#     request_by_donor = models.ForeignKey(
#         dmodels.Donor, null=True, on_delete=models.CASCADE)
#     patient_name = models.CharField(max_length=15)
#     patient_age = models.PositiveIntegerField()
#     reason = models.CharField(max_length=500)
#     bloodgroup = models.CharField(max_length=10)
#     unit = models.PositiveIntegerField(max_length=2, default=0)
#     status = models.CharField(max_length=20, default="Pending")
#     date = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.bloodgroup


from django.core.exceptions import ValidationError
from django.db import models
from patient import models as pmodels
from donor import models as dmodels


class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(max_length=2)

    def __str__(self):
        return self.bloodgroup


class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(
        pmodels.Patient, null=True, on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(
        dmodels.Donor, null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=15)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(max_length=2, default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def clean(self):
        if self.patient_age > 100:
            raise ValidationError("Age cannot be more than 100.")

    def __str__(self):
        return self.bloodgroup
