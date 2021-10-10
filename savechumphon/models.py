import datetime
from django.utils import timezone
from django.db import models
from django.db.models.fields.related import ForeignKey
from PIL import Image

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Duty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Occupation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Reason(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cchangwat(models.Model):
    changwatcode = models.CharField(max_length=2)
    changwatname = models.CharField(max_length=155)
    zonecode = models.CharField(max_length=2)
    changwatname_en = models.CharField(max_length=155)

    def __str__(self):
        return self.changwatname

class Campur(models.Model):
    ampurcode = models.CharField(max_length=2)
    ampurname = models.CharField(max_length=155)
    ampurcodefull = models.CharField(max_length=4)
    changwatcode = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)

    def __str__(self):
        return self.ampurname

class Ctambon(models.Model):
    tamboncode = models.CharField(max_length=2)
    tambonname = models.CharField(max_length=155)
    tamboncodefull = models.CharField(max_length=6)
    ampurcode = models.ForeignKey(Campur, on_delete=models.CASCADE)
    changwatcode = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)

    def __str__(self):
        return self.tambonname

class Vaccine1(models.Model):
    dose = models.CharField(max_length=2)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.dose+' - '+self.name

class Vaccine2(models.Model):
    dose = models.CharField(max_length=2)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.dose+' - '+self.name

class Savechumphon(models.Model):
    sex = (
        ('1','ชาย'),
        ('2','หญิง'),
    )

    close_contact = (
        ('1','เคยใกล้ชิด'),
        ('2','ไม่เคยใกล้ชิด'),
    )

    sign = (
        ('1','มีอาการ'),
        ('2','ไม่มีอาการ'),
    )
    
    history = (
        ('1','เคย'),
        ('2','ไม่เคย'),
    )

    between = (
        ('1','ประจวบคีรีขันธ์'),
        ('2','ระนอง'),
        ('3','สุราษฎร์ธานี'),
    )

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=sex, default='ชาย')
    age = models.IntegerField()
    id_card = models.CharField(max_length=15)
    mobile_phone = models.CharField(max_length=10)
    mobile_partner = models.CharField(max_length=10, null=True, blank=True)
    date_arrive = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Cchangwat = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)
    close_contact = models.CharField(max_length=25, choices=close_contact, default='ไม่เคยใกล้ชิด')
    sign = models.CharField(max_length=25, default='ไม่มีอาการ')
    history = models.CharField(max_length=25, default='ไม่เคย')
    ampur = models.ForeignKey(Campur, on_delete=models.CASCADE)
    moo = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=255)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    between = models.CharField(max_length=155,choices=between)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    stay = models.IntegerField()
    duty_place = models.TextField()
    vaccinate1 = models.ForeignKey(Vaccine1, on_delete=models.CASCADE)
    vaccinate2 = models.ForeignKey(Vaccine2, on_delete=models.CASCADE)
    vaccine_pic = models.ImageField(default= 'default.jpg', upload_to = 'vaccine_pic')
    sickness = models.ImageField(default = 'default.jpg', upload_to = 'sickness')
    lab = models.ImageField(default='default.jpg', upload_to = 'lab')
    input_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Savechumphon, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname+' - '+self.lname+' - '+self.id_card+' - '+self.ampur