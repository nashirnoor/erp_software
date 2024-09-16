from django.db import models
from apps.users.models import User


class Client(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ClientRequest(models.Model):
    COMPANY_SIZE_CHOICES = [
        ("small", "0 - 10"),
        ("medium", "10 - 50"),
        ("large", "50 - 100"),
        ("corporate", "Above 100"),
    ]

    PLATFORM_CHOICES = [
        ("zoom", "Zoom"),
        ("google_meet", "Google Meet"),
        ("microsoft_teams", "Microsoft Teams"),
        ("phone", "Phone Call"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("cancelled", "Cancelled"),
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
    ]

    assigned_staff = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    client_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255)
    scheduled_date = models.DateTimeField()
    company_size = models.CharField(max_length=20, choices=COMPANY_SIZE_CHOICES)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    service_requested = models.CharField(max_length=255)

    def __str__(self):
        return f"Demo Request for {self.company_name} on {self.scheduled_date}"


class ClientRelationship(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    CARE_OF_CHOICES = [
        ("nasscript", "Nasscript"),
        ("hisaan", "Hisaan"),
    ]

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="relationships"
    )
    products = models.JSONField()  # Store as a list of product identifiers
    reminder_date = models.DateField(null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    care_of = models.CharField(
        max_length=20, choices=CARE_OF_CHOICES, default="nasscript"
    )
    short_note = models.CharField(max_length=255, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.name} - {self.get_status_display()}"
