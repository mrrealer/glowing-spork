from __future__ import unicode_literals

from django.db import models

class Prospect(models.Model):
#PROSPECTIVE CUSTOMER INFORMATION
  prospectfn = models.CharField(max_length=30)
  prosepectln = models.CharField(max_length=30)
  #RELATIONSHIP TO PROSPECTIVE CUSTOMER
  recipientreltoProspect_mother = models.BooleanField(default=False)
  recipientreltoProspect_father = models.BooleanField(default=False)
  recipientreltoProspect_husband = models.BooleanField(default=False)
  recipientreltoProspect_wife = models.BooleanField(default=False)
  recipientreltoProspect_grandmother = models.BooleanField(default=False)
  recipientReltoProspect_grandfather = models.BooleanField(default=False)
  recipientReltoProspect_other = models.BooleanField(default=False)
  recipientReltoProspect_myself = models.BooleanField(default=False)
  #PREFERRED GENDER
  noGenderPreference = models.BooleanField(default=False) 
  femalePreference = models.BooleanField(default=False) 
  malePreference = models.BooleanField(default=False)
  #WHEN AND WHERE DO YOU NEED CARE?
  care_county_Brooklyn = models.BooleanField(default=False)
  care_county_Bronx = models.BooleanField(default=False)
  care_county_Manahattan = models.BooleanField(default=False) 
  care_county_StatenIsland = models.BooleanField(default=False) 
  care_county_Queens = models.BooleanField(default=False)
  care_county_Westchester = models.BooleanField(default=False) 
  emergencyCoverage = models.BooleanField(default=False)
  preferredLanguage_English = models.BooleanField(default=False)
  preferredLanguage_Spanish = models.BooleanField(default=False)
  preferredLanguage_Yiddish = models.BooleanField(default=False)
  preferredLanguage_HatianCreole = models.BooleanField(default=False) 
  preferredLanguage_Russian = models.BooleanField(default=False)
  preferredLanguage_Usbek = models.BooleanField(default=False)
  #REQUESTED SCHEDULE BROAD#
  #24 HOUR CARE REQUEST?
  _24hourCare = models.BooleanField(default=False) 
  duration_one_time = models.BooleanField(default=False) 
  long_term = models.BooleanField(default=False) 
  short_term = models.BooleanField(default=False)
  #APPROXIMATE TIME OF NEED
  careNeeded_now = models.BooleanField(default=False) 
  careNeeded_this_week = models.BooleanField(default=False) 
  careNeeded_this_month = models.BooleanField(default=False) 
  careNeeded_next_month = models.BooleanField(default=False)
  careNeeded_not_sure = models.BooleanField(default=False)
  #EXTRA THINGS WE SHOULD KNOW 
  specialCareNeeds = models.TextField(max_length=300)
  #REQUESTED SCHUEDULE SPECIFIC#
  # Day of Shift Starts
  dayShiftStarts_Monday = models.BooleanField(default=False)
  dayShiftStarts_Tuesday = models.BooleanField(default=False)
  dayShiftStarts_Wednesday = models.BooleanField(default=False)
  dayShiftStarts_Thursday = models.BooleanField(default=False)
  dayShiftStarts_Friday = models.BooleanField(default=False)
  dayShiftStarts_Saturday = models.BooleanField(default=False) 
  dayShiftStarts_Sunday = models.BooleanField(default=False)
  # Time Shift Starts 
  startShift_12am = models.BooleanField(default=False)
  startShift_1am = models.BooleanField(default=False)
  startShift_2am = models.BooleanField(default=False)
  startShift_3am = models.BooleanField(default=False)
  startShift_4am = models.BooleanField(default=False)
  startShift_5am = models.BooleanField(default=False)
  startShift_6am = models.BooleanField(default=False)
  startShift_7am = models.BooleanField(default=False)
  startShift_8am = models.BooleanField(default=False)
  startShift_9am = models.BooleanField(default=False)
  startShift_10am = models.BooleanField(default=False)
  startShift_11am = models.BooleanField(default=False)
  startShift_12pm = models.BooleanField(default=False)
  startShift_1pm = models.BooleanField(default=False)
  startShift_2pm = models.BooleanField(default=False)
  startShift_3pm = models.BooleanField(default=False)
  startShift_4pm = models.BooleanField(default=False)
  startShift_5pm = models.BooleanField(default=False)
  startShift_6pm = models.BooleanField(default=False)
  startShift_7pm = models.BooleanField(default=False)
  startShift_8pm = models.BooleanField(default=False)
  startShift_9pm = models.BooleanField(default=False)
  startShift_10pm = models.BooleanField(default=False)
  startShift_11pm = models.BooleanField(default=False)
  #Day Shift Ends
  dayShiftEnds_Monday = models.BooleanField(default=False)
  dayShiftEnds_Tuesday = models.BooleanField(default=False)
  dayShiftEnds_Wednesday = models.BooleanField(default=False)
  dayShiftEnds_Thursday = models.BooleanField(default=False)
  dayShiftEnds_Friday = models.BooleanField(default=False)
  dayShiftEnds_Saturday = models.BooleanField(default=False) 
  dayShiftEnds_Sunday = models.BooleanField(default=False)
  #Time Shift Ends
  endShift_12am = models.BooleanField(default=False)
  endShift_1am = models.BooleanField(default=False)
  endShift_2am = models.BooleanField(default=False)
  endShift_3am = models.BooleanField(default=False)
  endShift_4am = models.BooleanField(default=False)
  endShift_5am = models.BooleanField(default=False)
  endShift_6am = models.BooleanField(default=False)
  endShift_7am = models.BooleanField(default=False)
  endShift_8am = models.BooleanField(default=False)
  endShift_9am = models.BooleanField(default=False)
  endShift_10am = models.BooleanField(default=False)
  endShift_11am = models.BooleanField(default=False)
  endShift_12pm = models.BooleanField(default=False)
  endShift_1pm = models.BooleanField(default=False)
  endShift_2pm = models.BooleanField(default=False)
  endShift_3pm = models.BooleanField(default=False)
  endShift_4pm = models.BooleanField(default=False)
  endShift_5pm = models.BooleanField(default=False)
  endShift_6pm = models.BooleanField(default=False)
  endShift_7pm = models.BooleanField(default=False)
  endShift_8pm = models.BooleanField(default=False)
  endShift_9pm = models.BooleanField(default=False)
  endShift_10pm = models.BooleanField(default=False)
  endShift_11pm = models.BooleanField(default=False)
  #REGULAR CARE REQUESTED
  groceriesShopping = models.BooleanField(default=False) 
  cleaningHousekeeping = models.BooleanField(default=False) 
  hospiceCare = models.BooleanField(default=False)
  transportation = models.BooleanField(default=False) 
  overNightMonitoring = models.BooleanField(default=False) 
  companionCare = models.BooleanField(default=False) 
  personalCare = models.BooleanField(default=False)
  respiteCare = models.BooleanField(default=False)
  mealPreparation = models.BooleanField(default=False)
  #SPECIALTY CARE REQUESTED
  #This care costs more money
  deepCleaning = models.BooleanField(default=False) 
  woundCare = models.BooleanField(default=False) 
  als = models.BooleanField(default=False)
  parkinsonsDisease = models.BooleanField(default=False) 
  physicalTherapy = models.BooleanField(default=False)
  copd = models.BooleanField(default=False) 
  alzheimersDementia = models.BooleanField(default=False)
  #ADDRESS OF CARE RENDERING
  addressBuilding = models.CharField(max_length=30)
  addressStreet = models.CharField(max_length=30)
  addressApartment = models.CharField(max_length=30)
  addressCity = models.CharField(max_length=30)
  addressState = models.CharField(max_length=30)
  addressZip = models.CharField(max_length=30)
  #ALREADY A CUSTOMER?




#RECIPIENT OF CARE INFORMATION
class Recipient(models.Model):
  recipientfn=models.CharField(max_length=30)
  recipientln=models.CharField(max_length=30)

