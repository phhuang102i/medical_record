from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import datetime
from . import freq_type

# Create your models here.
from django.contrib.auth.models import User

class Illness(models.Model):
    name = models.CharField(max_length = 200,help_text = "輸入疾病名稱")
    Type = (('severe','重大疾病'),('minor','一般疾病'))
    selection = models.CharField(choices = Type,max_length = 10,default ='minor',help_text = '請選疾病是否為重症')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('illness-detail',args = [str(self.id)])
    def get_update_url(self):
        return reverse('illness_update',args = [str(self.id)])
    def get_delete_url(self):
        return reverse('illness_delete',args = [str(self.id)])
    class Meta:
        permissions = (("doctor", "Update or delete"),) 
class Severe_illness_record(models.Model):
    date = models.DateField(help_text = "發病日期",default = datetime.date.today)
    patient = models.ForeignKey('Patient',on_delete = models.SET_NULL,null = True,help_text = "病人姓名")
    illness = models.OneToOneField(Illness,help_text = "重症名稱", on_delete = models.CASCADE)
    class Meta:
        permissions = (("doctor", "Update or delete"),)
        
	
    def __str__(self):
        return str(self.patient)+" "+str(self.illness) + " " + str(self.date)


class Treatment_record(models.Model):
    treatment_detail = models.TextField(max_length = 400,help_text = "診斷紀錄", blank = True)
    date = models.DateField(help_text = "診斷日期")
    patient = models.ForeignKey('Patient',on_delete=models.SET_NULL, null=True, blank = True)
    
    class Meta:
        ordering = ['date']
        permissions = (("doctor", "Update or delete"),)
    def __str__(self):
        return self.treatment_detail
    def get_create_url(self,patient_id):
        return reverse('treatment_record_create',args = [str(patient_id)])

class Medication(models.Model):
    name = models.CharField(max_length = 200,help_text = "藥物名稱")
    duration = models.PositiveIntegerField(default = 1,help_text ="服用時間(周)")
    treatment = models.ForeignKey('Treatment_record',on_delete=models.CASCADE,null= True)
    
    freq = models.CharField(choices = freq_type.FreqType.freq_type,max_length = 200,help_text = "請選擇藥物使用頻率")	
    class Meta:
        permissions = (("doctor", "Update or delete"),)	


class Patient(models.Model):
    name = models.CharField(max_length = 200,help_text = "輸入病人姓名")
    personalid = models.CharField(max_length = 200,help_text = "輸入病人身分證字號")
    bloodtype = models.CharField(max_length = 200,help_text = "輸入病人血型")
    height = models.PositiveIntegerField(help_text ="輸入病人身高(cm)",default = 180)
    weight = models.PositiveIntegerField(help_text = "輸入病人體重(kg)",default = 70)
    date_of_birth = models.DateField(help_text = "輸入病人出生年月日")
    return_date = models.DateField(help_text = "下次約診日期", blank = True, default = datetime.date.today) 
    illness = models.ManyToManyField(Illness,help_text = "請選病人患有什麼疾病",related_name ="illness")
    past_illness = models.ManyToManyField(Illness,help_text = "請選病人過去病史",related_name = "past_illness")
    class Meta:
        permissions = (("doctor", "Update or delete"),)
    def BMI(self):
        return round(float(self.weight)/((float(self.height)/100)** 2),2)   
	

    def __str__(self):
        return (self.name+", ID = "+self.personalid)

    def return_id(self):
        return self.id
    def get_absolute_url(self):
        return reverse('patient-detail',args = [str(self.id)])
    def get_update_url(self):
        return reverse('patient_update',args = [str(self.id)])
    def get_delete_url(self):
        return reverse('patient_delete',args = [str(self.id)])

