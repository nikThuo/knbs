from django.db import models

# Create your models here.
class Arrivals(models.Model):
    arrivals_id = models.AutoField(primary_key=True)
    quarter = models.CharField(max_length=100)
    holiday = models.DecimalField(max_digits=15, decimal_places=2)
    business = models.DecimalField(max_digits=15, decimal_places=2)
    transit = models.DecimalField(max_digits=15, decimal_places=2)
    other = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.DateField()

class Conferences(models.Model):
    conference_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    number_of_conferences = models.DecimalField(max_digits=15, decimal_places=2)
    number_of_delegates = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.DateField()

class Departures(models.Model):
    departures_id = models.AutoField(primary_key=True)
    quarter = models.CharField(max_length=100)
    holiday = models.DecimalField(max_digits=15, decimal_places=2)
    business = models.DecimalField(max_digits=15, decimal_places=2)
    transit = models.DecimalField(max_digits=15, decimal_places=2)
    other = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.DateField()

class Earnings(models.Model):
    earnings_id = models.AutoField(primary_key=True)
    tourism_earnings_billions = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.DateField()

class Hotel_Occupancy_By_Residence(models.Model):
    hotel_occupancy_id = models.AutoField(primary_key=True)
    year = models.DateField()
    permanent_occupants = models.DecimalField(max_digits=30, decimal_places=3)
    germany = models.DecimalField(max_digits=30, decimal_places=3)
    switzerland = models.DecimalField(max_digits=30, decimal_places=3)
    united_kingdom = models.DecimalField(max_digits=30, decimal_places=3)
    italy = models.DecimalField(max_digits=30, decimal_places=3)
    france = models.DecimalField(max_digits=30, decimal_places=3)
    scandinavia = models.DecimalField(max_digits=30, decimal_places=3)
    other_europe = models.DecimalField(max_digits=30, decimal_places=3)
    europe = models.DecimalField(max_digits=30, decimal_places=3)
    kenya_residents = models.DecimalField(max_digits=30, decimal_places=3)
    uganda = models.DecimalField(max_digits=30, decimal_places=3)
    tanzania = models.DecimalField(max_digits=30, decimal_places=3)
    east_and_central_africa = models.DecimalField(max_digits=30, decimal_places=3)
    west_africa = models.DecimalField(max_digits=30, decimal_places=3)
    north_africa = models.DecimalField(max_digits=30, decimal_places=3)
    south_africa = models.DecimalField(max_digits=30, decimal_places=3)
    other_africa = models.DecimalField(max_digits=30, decimal_places=3)
    africa = models.DecimalField(max_digits=30, decimal_places=3)
    usa = models.DecimalField(max_digits=30, decimal_places=3)
    canada = models.DecimalField(max_digits=30, decimal_places=3)
    other_america = models.DecimalField(max_digits=30, decimal_places=3)
    america = models.DecimalField(max_digits=30, decimal_places=3)
    japan = models.DecimalField(max_digits=30, decimal_places=3)
    india = models.DecimalField(max_digits=30, decimal_places=3)
    middle_east = models.DecimalField(max_digits=30, decimal_places=3)
    other_asia = models.DecimalField(max_digits=30, decimal_places=3)
    asia = models.DecimalField(max_digits=30, decimal_places=3)
    australia_and_new_zealand = models.DecimalField(max_digits=30, decimal_places=3)
    all_other_countries = models.DecimalField(max_digits=30, decimal_places=3)
    total_occupied = models.DecimalField(max_digits=30, decimal_places=3)
    total_available = models.DecimalField(max_digits=30, decimal_places=3)
    occupancy_percentage_rate = models.DecimalField(max_digits=30, decimal_places=10)

class Hotel_Occupancy_By_Zone(models.Model):
    year = models.DateField()
    coastal_beach = models.DecimalField(max_digits=30, decimal_places=3)
    coastal_other = models.DecimalField(max_digits=30, decimal_places=3)
    coastal_hinterland = models.DecimalField(max_digits=30, decimal_places=3)
    nairobi_high_class = models.DecimalField(max_digits=30, decimal_places=3)
    nairobi_other = models.DecimalField(max_digits=30, decimal_places=3)
    central = models.DecimalField(max_digits=30, decimal_places=3)
    masailand = models.DecimalField(max_digits=30, decimal_places=3)
    nyanza_basin = models.DecimalField(max_digits=30, decimal_places=3)
    western = models.DecimalField(max_digits=30, decimal_places=3)
    northern = models.DecimalField(max_digits=30, decimal_places=3)
    total_occupied = models.DecimalField(max_digits=30, decimal_places=3)
    total_available = models.DecimalField(max_digits=30, decimal_places=3)

class Visitor_To_Parks(models.Model):
    visitor_parks_id = models.AutoField(primary_key=True)
    year = models.DateField()
    nairobi = models.DecimalField(max_digits=30, decimal_places=3)
    nairobi_safari_walk = models.DecimalField(max_digits=30, decimal_places=3)
    nairobi_mini_orphanage = models.DecimalField(max_digits=30, decimal_places=3)
    amboseli = models.DecimalField(max_digits=30, decimal_places=3)
    tsavo_west = models.DecimalField(max_digits=30, decimal_places=3)
    tsavo_east = models.DecimalField(max_digits=30, decimal_places=3)
    aberdare = models.DecimalField(max_digits=30, decimal_places=3)
    lake_nakuru = models.DecimalField(max_digits=30, decimal_places=3)
    masai_mara = models.DecimalField(max_digits=30, decimal_places=3)
    hallers_park = models.DecimalField(max_digits=30, decimal_places=3)
    malindi_marine = models.DecimalField(max_digits=30, decimal_places=3)
    lake_bogoria = models.DecimalField(max_digits=30, decimal_places=3)
    meru = models.DecimalField(max_digits=30, decimal_places=3)
    shimba_hills = models.DecimalField(max_digits=30, decimal_places=3)
    mt_kenya = models.DecimalField(max_digits=30, decimal_places=3)
    samburu = models.DecimalField(max_digits=30, decimal_places=3)
    kisite_mpunguti = models.DecimalField(max_digits=30, decimal_places=3)
    mombasa_marine = models.DecimalField(max_digits=30, decimal_places=3)
    watamu_marine = models.DecimalField(max_digits=30, decimal_places=3)
    hells_gate = models.DecimalField(max_digits=30, decimal_places=3)
    impala_sanctuary_kisumu = models.DecimalField(max_digits=30, decimal_places=3)
    mt_longonot = models.DecimalField(max_digits=30, decimal_places=3)
    other = models.DecimalField(max_digits=30, decimal_places=3)

class Visitors_To_Museums(models.Model):
    visitor_museums_id = models.AutoField(primary_key=True)
    year = models.DateField()
    nairobi_snake_park = models.DecimalField(max_digits=30, decimal_places=3)
    fort_jesus = models.DecimalField(max_digits=30, decimal_places=3)
    kisumu = models.DecimalField(max_digits=30, decimal_places=3)
    kitale = models.DecimalField(max_digits=30, decimal_places=3)
    gede = models.DecimalField(max_digits=30, decimal_places=3)
    meru = models.DecimalField(max_digits=30, decimal_places=3)
    lamu = models.DecimalField(max_digits=30, decimal_places=3)
    jumba_la_mtwana = models.DecimalField(max_digits=30, decimal_places=3)
    kariandusi = models.DecimalField(max_digits=30, decimal_places=3)
    hyrax_hill = models.DecimalField(max_digits=30, decimal_places=3)
    karen_blixen = models.DecimalField(max_digits=30, decimal_places=3)
    malindi = models.DecimalField(max_digits=30, decimal_places=3)
    kilifi_mnarani = models.DecimalField(max_digits=30, decimal_places=3)
    kabarnet = models.DecimalField(max_digits=30, decimal_places=3)
    kapenguria = models.DecimalField(max_digits=30, decimal_places=3)
    swahili_house = models.DecimalField(max_digits=30, decimal_places=3)
    narok = models.DecimalField(max_digits=30, decimal_places=3)
    german_post = models.DecimalField(max_digits=30, decimal_places=3)
    takwa_ruins = models.DecimalField(max_digits=30, decimal_places=3)


############################################KIHBIS II ############################################

class Population_Proportion_That_Took_Trip(models.Model):
    population_id = models.AutoField(primary_key=True)
    county_id = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()
