from django.db import models
from enum import Enum
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Distribution(Enum):
    NORTH = 'Northern states'
    MIDDLE = 'Middle states'
    SOUTH = 'south'
    NORTH_MIDDLE = 'northern and middle states'
    MIDDLE_SOUTH = 'middle and southern states'


class NeedleCount(Enum):
    TWO = 2
    THREE = 3
    FIVE = 5


class NeedleLength(Enum):
    TWO_THREE = '2-3'
    TWO_FOUR = '2-4'
    THREE_FIVE = '3-5'
    THREE_SIX = '3-6'
    FOUR_SIX = '4-6'
    FOUR_EIGHT = '4-8'
    FIVE_ELEVEN = '5-11'
    SIX_NINE = '6-9'
    EIGHT_EIGHTEEN = '8-18'


class ConeLength(Enum):
    LARGE = 'longer than three inches'
    SHORT = 'shorter than three inches'
    BOTH = 'size can be plus or minus 3 inches'


class ConeShape(Enum):
    ROUND = 'round'
    LONG = 'Longer than Wide'
    WIDE = 'Wider than long'
    BOTH = 'larger axis varies'


class ConePrickles(Enum):
    THIN = 'thin'
    LACKING = 'lacking'
    THIN_LACKING = 'thin to lacking'
    STOUT = 'stout'


class PinusGenus(models.Model):
    NEEDLE_LENGTH_CHOICES = [(key, key.value)
                             for key in NeedleLength]
    NEEDLE_COUNT_CHOICES = [(key, key.value)
                            for key in NeedleCount]
    CONE_LENGTH_CHOICES = [(key, key.value)
                           for key in ConeLength]
    CONE_SHAPE_CHOICES = [(key, key.value) for key in ConeShape]
    CONE_PRICKLES_CHOICES = [(key, key.value)
                             for key in ConePrickles]
    DISTRIBUTION_CHOICES = [(key, key.value)
                            for key in Distribution]
    common_name = models.CharField(max_length=150)
    scientific_name = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)
    distribution = models.CharField(choices=DISTRIBUTION_CHOICES, max_length=60 )
    needle_count = models.IntegerField(choices = NEEDLE_COUNT_CHOICES )
    needle_length  = models.CharField(choices = NEEDLE_LENGTH_CHOICES, max_length=60 )
    old_cones = models.BooleanField()
    cone_length = models.CharField(choices = CONE_LENGTH_CHOICES, max_length=60 )
    cone_shape = models.CharField(choices = CONE_SHAPE_CHOICES, max_length=60 )
    cone_prickles = models.CharField(choices = CONE_PRICKLES_CHOICES, max_length=60 )
    twig_texture = models.BooleanField(null=True)
    fire_resilience = models.BooleanField(null=True)
    def __str__(self):
        return self.scientific_name

class PinusKey(models.Model):
  id = models.IntegerField(primary_key=True)
  characteristic_a = models.CharField(max_length=200)
  characteristic_b = models.CharField(max_length=200)
  parent= models.ForeignKey('self', on_delete=models.PROTECT, blank=True)
  child_a = models.ForeignKey(ContentType, on_delete=models.PROTECT, related_name='+')
  child_b = models.ForeignKey(ContentType, on_delete=models.PROTECT, related_name='+')
  object_id_a = models.PositiveIntegerField()
  object_id_b = models.PositiveIntegerField()
  choose_a = GenericForeignKey('child_a', 'object_id_a') 
  choose_b = GenericForeignKey('child_b', 'object_id_b')