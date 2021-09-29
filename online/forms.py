from django import forms
from django.forms import widgets
from online.models import registermodel

def username(value):
    if not(2<=len(value)<=10): 
        raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")

def passs(pas):
    if not(pas[0].isupper()):
        raise forms.ValidationError("plz enter the first character should be uppercase")
    for i in pas:
        if not('A'<=i<='Z' or 'a'<=i<='z'):
            break
    else:
        raise forms.ValidationError("plz atleast one digit")
    for i in pas:
        if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
            break
    else:
        raise forms.ValidationError("plz atleast one special character")

class registerform(forms.ModelForm):
    class Meta:
        model = registermodel
        fields = '__all__'
        

    lastname = forms.CharField(widget=forms.TextInput,validators=[username,passs])
    '''
    def clean(self):
        un= self.cleaned_data['username']
        if not(3<=len(un)<=10): 
            raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")

        fn= self.cleaned_data['firstname']
        if not(3<=len(fn)<=10): 
            raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")
        
        gn= self.cleaned_data['gender']
        if not(4<=len(gn)<=6): 
            raise forms.ValidationError("plz enter the min 4 characters and max 6 characters")
        
        ag= self.cleaned_data['age']
        if not(10<=ag<=60): 
            raise forms.ValidationError("plz enter the age min 10 and max 60 characters")

        ph= self.cleaned_data['phone']
        if not(len(str(ph))==10):
            raise forms.ValidationError("plz enter the  10 digits")

        pas= self.cleaned_data['password']
        if not(pas[0].isupper()):
            raise forms.ValidationError("plz enter the first character should be uppercase")
        for i in pas:
            if not('A'<=i<='Z' or 'a'<=i<='z'):
                break
        else:
            raise forms.ValidationError("plz atleast one digit")
        for i in pas:
            if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
                break
        else:
            raise forms.ValidationError("plz atleast one special character")

    '''

    
    
    '''
    
    def clean_username(self):
        res= self.cleaned_data['username']
        if not(3<=len(res)<=10): 
            raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")
        return res

    def clean_firstname(self):
        res= self.cleaned_data['firstname']
        if not(3<=len(res)<=10): 
            raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")
        return res

    def clean_gender(self):
        res= self.cleaned_data['gender']
        if not(4<=len(res)<=6): 
            raise forms.ValidationError("plz enter the min 4 characters and max 6 characters")
        return res

    def clean_age(self):
        res= self.cleaned_data['age']
        if not(10<=res<=60): 
            raise forms.ValidationError("plz enter the age min 10 and max 60 characters")
        return res
    def clean_phone(self):
        res= self.cleaned_data['phone']
        if not(len(str(res))==10):
            raise forms.ValidationError("plz enter the  10 digits")
        return res

    def clean_password(self):
        res= self.cleaned_data['password']
        if not(res[0].isupper()):
            raise forms.ValidationError("plz enter the first character should be uppercase")
        return res
    '''