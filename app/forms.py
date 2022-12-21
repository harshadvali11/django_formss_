from django import forms
g=[('MALE','m'),('FEMALE','FM')]
c=[('PYTHON','python'),('DJANGO','django'),('SQL','sql'),('HTML','html')]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #address=forms.CharField(max_length=1000,widget=forms.Textarea)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)