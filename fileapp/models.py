from django.db import models

class UploadedFile(models.Model):
    CATEGORY_CHOICES = (
        ('TDL', 'TDL'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="file_images/", blank=True, null=True)
    file = models.FileField(upload_to="files/")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # phone = models.CharField(max_length=15)  # new field for phone number
    phone = models.CharField(max_length=15, default='0000000000')  # default 10-digit placeholder
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


