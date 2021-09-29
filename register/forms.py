from django import forms

class registerform(forms.Form):
    username =forms.CharField(widget=forms.TextInput,label= "USERNAME", max_length=10,min_length=3)
    firstname= forms.CharField(widget=forms.TextInput,initial='venugopal')
    '''
    email =forms.EmailField()
    list1=[('Male','MALE'),('Female','FEMALE')]
    gender =forms.ChoiceField(choices=list1,)
    gender1 =forms.ChoiceField(choices=list1, widget=forms.RadioSelect)
    gender2 =forms.ChoiceField(choices=list1, widget=forms.CheckboxSelectMultiple)
    dob= forms.DateField(widget=forms.SelectDateWidget)
    dob= forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    dob1= forms.DateField(widget=forms.DateInput)
    bi=['2019','2020','2021','2022']
    dob2= forms.DateField(widget=forms.SelectDateWidget(years=bi))

    age= forms.IntegerField()
    sal=forms.FloatField()
    sal1=forms.DecimalField()
    phone=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)
    password =forms.CharField(widget=forms.PasswordInput)
    repassword =forms.CharField(widget=forms.PasswordInput)
    pic= forms.ImageField()
    file= forms.FileField()
    '''