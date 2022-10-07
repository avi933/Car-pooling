from statistics import mode
from django.db import models

# Create your models here.

    



vendor_status_choices = (
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Hold', 'Hold'),
    ('Temp Approved', 'Temp Approved'),
)
class vendorprofile(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    status = models.CharField(max_length=8 , choices=vendor_status_choices, default = "Pending")
    full_name = models.CharField(max_length=256)

    
    image = models.ImageField(null=True, blank=True)
    dob = models.DateField()
    email = models.EmailField()
    contact1 = models.CharField(max_length=10)
    contact2 = models.CharField(max_length=10, blank=True, null=True)

    address = models.TextField()

   
    NIC_front = models.ImageField(blank=True, null=True)
    NIC_rear = models.ImageField(blank=True, null=True)
    driving_licence_front = models.ImageField(blank=True, null=True)
    driving_licence_rear = models.ImageField(blank=True, null=True)
    verified = models.BooleanField(default=0)
    rejection_reason = models.TextField(blank=True, null=True)
    date_of_registration = models.DateField(auto_now_add=True)
    total_4_seater = models.PositiveSmallIntegerField(default=0)
    total_7_seater = models.PositiveSmallIntegerField(default=0)
    total_15_seater= models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name_plural = 'Vendor Details'

    def get_approved_cars(self):
        cars = vendor_cars.objects.filter(vendor = self, status__in = ["Approved", "Temp Approved"])
        return cars

    def get_approved_drivers(self):
        cars = driver.objects.filter(vendor = self, status__in = ["Approved", "Temp Approved"])
        return cars


account_type_choices = (
    ('C', 'Current'),
    ('S', 'Saving'),
)


class bank_detail(models.Model):
    vendor = models.ForeignKey('vendor.vendorprofile', on_delete=models.PROTECT)
    account_holder_name = models.CharField(max_length=50, blank=True, null=True)
    account_no = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=1, choices=account_type_choices, blank=True, null=True)
    ifsc = models.CharField(max_length=20)
    bank_address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.vendor) + str(self.account_holder_name)

    class Meta:
        verbose_name_plural = 'Vendor Bank Details'

status_choices = (
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Hold', 'Hold'),
    ('Temp Approved', 'Temp Approved'),
)
fuel_type_choices = (
    ('P', 'Petrol'),
    ('D', 'Diesel'),
    ('C', 'CNG'),
)
class vendor_cars(models.Model):
    vendor = models.ForeignKey(vendorprofile, on_delete=models.PROTECT)
    car_type = models.ForeignKey('core.car_types', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=16 , choices=status_choices, default = "Pending")

    owner_name = models.CharField(max_length=256, blank=True, null=True)
    registration_no = models.CharField(max_length=50,blank=True, null=True)
    dateofregistration = models.DateField(blank=True, null=True)
    image_front = models.ImageField(blank=True, null=True)
    image_rear = models.ImageField(blank=True, null=True)
    insurance_front = models.ImageField(blank=True, null=True)
    insurance_valid_upto = models.DateField(blank=True, null=True)


    def __str__(self):
        return str(self.car_type) + ": " + str(self.registration_no)

    class Meta:
        verbose_name_plural = 'Vendor Cars'

driver_status_choices = (
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Hold', 'Hold'),
    ('Temp Approved', 'Temp Approved'),
)
class driver(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendorprofile, on_delete=models.PROTECT)
    status = models.CharField(max_length=16 , choices=status_choices, default = "Pending")
    full_name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    dob = models.DateField()

    email = models.EmailField()
    contact1 = models.CharField(max_length=10)
    contact2 = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField()

    NIC_front = models.ImageField()
    NIC_rear = models.ImageField()


    driving_licence_front = models.ImageField(blank=True, null=True)
    driving_licence_rear = models.ImageField(blank=True, null=True)
    driving_licence_no = models.CharField(max_length=50, blank=True, null=True)
    driving_licence_valid_from = models.DateField()


    legal_accidental_case = models.BooleanField(default=False)
    legal_accidental_case_details = models.TextField(blank=True, null=True)
    legal_accidental_case_document = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.full_name) + " (" + str(self.contact1) + ")"