from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    GENDERS = {
        1: "чоловік",
        2: "жінка"
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.IntegerField(choices=GENDERS, default=1, verbose_name=_('gender'))
    birth_date = models.DateField(verbose_name=_('date of birth'))

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

    @property
    def gender_display(self):
        return self.GENDERS[self.gender]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Tourist(Person):
    group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.SET_NULL)


class Amateur(Tourist):
    COMPLEXITY = {
        1: "Початкова",
        2: "Середня",
        3: "Висока"
    }
    qualification = models.IntegerField(choices=COMPLEXITY, default=1)


class Sportsman(Tourist):
    pass


class Section(models.Model):
    SPECS = {
        1: "водники",
        2: "спелеологи",
        3: "альпіністи",
        4: "пішоходи"
    }
    name = models.CharField(max_length=30, unique=True)
    type = models.IntegerField(choices=SPECS, default=4)

    @property
    def type_display(self):
        return self.SPECS[self.type]

    def __str__(self):
        return self.name

class Administration(models.Model):
    section = models.OneToOneField(
        'Section',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return str(self.section.name)

class Coach(Tourist):
    SPECS = {
        1: "водники",
        2: "спелеологи",
        3: "альпіністи",
        4: "пішоходи"
    }
    administration = models.ForeignKey('Administration', on_delete=models.CASCADE, verbose_name = _('Coach|administration'))
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=1000, verbose_name = _('Coach|salary'))
    spec = models.IntegerField(choices=SPECS, default=4)

    class Meta:
        verbose_name = _('coach')
        verbose_name_plural = _('coaches')


class Manager(Person):
    administration = models.OneToOneField(
        'Administration',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=1000)



class Group(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    coach = models.ForeignKey('Coach', related_name='groups', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.section.name


class Event(models.Model):
    place = models.CharField(max_length=30)
    date_from = models.DateField()
    date_to = models.DateField()
    coaches = models.ManyToManyField(Coach)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(date_to__gte=models.F("date_from")), name="date_gte"),
        ]


class Competition(Event):
    athletes = models.ManyToManyField('Sportsman')


class Training(Event):
    sections = models.ManyToManyField('Section')


class Instructor(models.Model):
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE, null=True, blank=True)
    sportsman = models.ForeignKey('Sportsman', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(coach=None) | models.Q(sportsman=None), name="not_both_null"),
        ]

    def __str__(self):
        if self.coach:
            return f"{self.coach.last_name}"
        else:
            return f"{self.sportsman.last_name}"

class Place(models.Model):
    CATEGORIES = {
        1: "Гори",
        2: "Водна",
        3: "Рівнина"
    }
    name = models.CharField(max_length=60)
    category = models.IntegerField(choices=CATEGORIES, default=3)


class Route(models.Model):
    from_place = models.ForeignKey('Place', related_name='routes_from', on_delete=models.CASCADE)
    to_place = models.ForeignKey('Place', related_name='routes_to', on_delete=models.CASCADE)
    places = models.ManyToManyField('Place', related_name='routes_point')
    distance = models.IntegerField(null=False)


class Tour(Event):
    COMPLEXITY = {
        1: "Початкова",
        2: "Середня",
        3: "Висока"
    }
    TYPES = {
        1: "піший",
        2: "кінний",
        3: "водний",
        4: "гірський"
    }
    instructor = models.ForeignKey('Person', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    complexity = models.IntegerField(choices=COMPLEXITY, default=1)
    type = models.IntegerField(choices=TYPES, default=1)
    tourists = models.ManyToManyField('Tourist', related_name='tours')
