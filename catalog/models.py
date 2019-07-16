from django.db import models
import datetime

# Create your models here.
class Illness(models.Model):
    name = models.CharField(max_length = 200,help_text = "輸入疾病名稱")

    def __str__(self):
        return self.name


class Treatment_record(models.Model):
    treatment_detail = models.TextField(max_length = 400,help_text = "診斷紀錄", blank = True)
    date = models.DateField(help_text = "診斷日期")
    patient = models.ForeignKey('Patient',on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.treatment_detail

		
class Patient(models.Model):
    name = models.CharField(max_length = 200,help_text = "輸入病人姓名")
    personalid = models.CharField(max_length = 200,help_text = "輸入病人身分證字號")
    bloodtype = models.CharField(max_length = 200,help_text = "輸入病人血型")
    date_of_birth = models.DateField(help_text = "輸入病人出生年月日")
    return_date = models.DateField(help_text = "下次約診日期", blank = True, default = datetime.date.today)
    
    illness = models.ManyToManyField(Illness,help_text = "請選病人患有什麼疾病")
	
    
	
    
    def __str__(self):
        return (self.name+", ID = "+self.personalid)

    def get_absolute_url(self):
        return reverse('patient-detail',args = [str(self.id)])






	
	
	
	
	
	
	
	
	
	
	