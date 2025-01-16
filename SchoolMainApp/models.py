from django.db import models

class Page(models.Model):
    purpose = models.CharField(max_length=100, default="General")
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, default="")
    long_description = models.TextField(default="")

    def __str__(self) -> str:
        return self.title


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.middle_name + " " + self.last_name



class RegistrationInfo(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    childFirstName = models.CharField(max_length=50)
    childLastName = models.CharField(max_length=50)
    childAge = models.IntegerField()

    SUBJECT_CHOICES = [('rusLang', 'Русский язык'), ('paint', 'Рисование'), ('bookClub', 'Книжный клуб'), ('hist', 'История'), ('mus', 'Музыка'), ('musArt', 'Музыкально-Театральная Студия'), ('chess', 'Шахматы'), ('prog', 'Программирование'), ]

    def __str__(self) -> str:
        return self.email