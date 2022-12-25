from django.db import models

# Create your models here.
class HomeDeets(models.Model):
    home_id = models.IntegerField(primary_key=True)
    price = models.IntegerField(default=0)
    square_ft = models.IntegerField(default=0)
    beds = models.IntegerField(default = 0)
    baths = models.IntegerField(default=0)
    garage_spaces = models.IntegerField(default=0)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    lot_size = models.IntegerField(default=0)
    year_built = models.IntegerField(default=0)
    days_listed = models.IntegerField(default=0)
    c_test_field = models.IntegerField(default=0)

    def __str__(self):
        return (self.house_name)

    @property
    def house_name(self):
        return '%s %s %s' % (self.street_address, self.city, self.state)
    
    def save(self):
        self.street_address = self.street_address.upper()

    