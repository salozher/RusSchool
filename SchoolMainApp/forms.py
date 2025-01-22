from django import forms

SUBJECT_CHOICES = [
    ('Русский язык', 'Русский язык'),
    ('Рисование', 'Рисование'),
    ('Книжный клуб', 'Книжный клуб'),
    ('История', 'История'),
    ('Музыка', 'Музыка'),
    ('Музыкально-Театральная Студия', 'Музыкально-Театральная Студия'),
    ('Шахматы', 'Шахматы'),
    ('Программирование', 'Программирование'),
]

class Contact(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    kids_age = forms.IntegerField(
        label="Kids Age",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kids Age'})
    )
    subjects = forms.MultipleChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Select Subjects"
    )

    def __str__(self) -> str:
        return self.email
