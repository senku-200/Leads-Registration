from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


CHOICES = [
    ('GenAI','GenAI'),
    ('Computer Vision','Computer Vision'),
    ('Predictive Maintenance','Predictive Maintenance'),
    ('ESG','ESG'),
    ('Others','Others'),
]



class Lead(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name='Full Name',
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)]
    )
    company_name = models.CharField(
        max_length=255,
        verbose_name='Company Name',
        blank=False,
        null=False,
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        blank=False,
        null=False
    )
    contact_number = PhoneNumberField(
        verbose_name='Contact Number',
        blank=False,
        null=False
    )
    service_description = models.TextField(
        verbose_name='Service Description',
        blank=False,
        null=False
    )
    category = models.CharField(
        max_length=255,
        verbose_name='Service Category',
        choices = CHOICES
    )
    custom_category = models.CharField(
        max_length=255,
        verbose_name='Custom Category',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        verbose_name = 'lead'
        verbose_name_plural = 'leads'
        ordering = ["-updated_at", "-created_at"]
        indexes = [
            models.Index(fields=['email'], name='email_idx'),
        ]

    def __str__(self):
        return f"{self.full_name} ({self.email})"
