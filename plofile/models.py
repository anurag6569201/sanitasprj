from django.db import models
from userauths.models import User
    
class Sanitizer(models.Model):
    CITY_CHOICES = (
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Maihar', 'Maihar'),
    ('Cuttack', 'Cuttack'),
    ('Rourkela', 'Rourkela'),
    ('Puri', 'Puri'),
    ('Sambalpur', 'Sambalpur'),
    ('Brahmapur', 'Brahmapur'),
    ('Balasore', 'Balasore'),
    ('Jharsuguda', 'Jharsuguda'),
    ('Baripada', 'Baripada'),
    ('Bargarh', 'Bargarh'),
)

    STATE_CHOICES = (
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sanitizer')
    name = models.CharField(max_length=100, default="Aims Hospital")
    street = models.CharField(max_length=255, default="Street 99")
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default="City 99")
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default="State 99")
    zip = models.CharField(max_length=20, default="XXXXXX")
    contactperson = models.CharField(max_length=100, default="Virju")
    phone = models.CharField(max_length=10, default="XXXXXXXXXX")
    email = models.EmailField(default="example@example.com")
    profile_image = models.ImageField(upload_to='Sanitizerprofile/')
    
    CPphone = models.CharField(max_length=10, default="XXXXXXXXXX")
    CPemail = models.EmailField(default="example@example.com")

    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    
    certificate = models.ImageField(upload_to='sanitizerDoc/',blank=True)
    isChecked = models.BooleanField(default=True)
    isSubmitted = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)

class TrendingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=Sanitizer.STATE_CHOICES)
    city = models.CharField(max_length=100, choices=Sanitizer.CITY_CHOICES)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

class Disease(models.Model):
    trending_data = models.ForeignKey(TrendingData, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cases = models.IntegerField()