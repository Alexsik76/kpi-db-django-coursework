from django.db import models
from django.utils import timezone


class Person(models.Model):
    GENDERS = {
        1: "чоловік",
        2: "жінка"
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.IntegerField(choices=GENDERS, default=1)
    birth_date = models.DateField()

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age


class Tourist(Person):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    category = models.ForeignKey('Complexity', on_delete=models.CASCADE)


class Amateur(Tourist):
    pass


class Sportsman(Tourist):
    pass


class Section(models.Model):
    name = models.CharField(max_length=30, unique=True)
    type = models.ForeignKey('Specs', on_delete=models.CASCADE)


class Administration(models.Model):
    section = models.OneToOneField(
        Section,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Specs(models.Model):
    SPECS = {
        1: "водники",
        2: "спелеологи",
        3: "альпіністи",
        4: "пішоходи"
    }
    value = models.IntegerField(choices=SPECS.items(), default=41)


class Coach(Tourist):
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    spec = models.ForeignKey(Specs, on_delete=models.CASCADE)


class Manager(Person):
    administration = models.OneToOneField(
        Administration,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    salary = models.DecimalField(max_digits=20, decimal_places=2)


class Group(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, related_name='groups', on_delete=models.CASCADE)


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
    athletes = models.ManyToManyField(Sportsman)


class Training(Event):
    sections = models.ManyToManyField(Section)


class Instructor(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)
    sportsman = models.ForeignKey(Sportsman, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(coach=None) | models.Q(sportsman=None), name="not_both_null"),
        ]


class Place(models.Model):
    CATEGORIES = {
        1: "Гори",
        2: "Водна",
        3: "Рівнина"
    }
    name = models.CharField(max_length=60)
    category = models.IntegerField(choices=CATEGORIES, default=3)


class Route(models.Model):
    from_place = models.ForeignKey(Place, related_name='routes_from', on_delete=models.CASCADE)
    to_place = models.ForeignKey(Place, related_name='routes_to', on_delete=models.CASCADE)
    places = models.ManyToManyField(Place, related_name='routes_point')
    distance = models.IntegerField(null=False)


class Complexity(models.Model):
    COMPLEXITY = {
        1: "Початкова",
        2: "Середня",
        3: "Висока"
    }
    value = models.IntegerField(choices=COMPLEXITY, default=1)


class Spec(models.Model):
    TYPES = {
        1: "піший",
        2: "кінний",
        3: "водний",
        4: "гірський"
    }
    value = models.IntegerField(choices=TYPES, default=1)


class Tour(Event):
    instructor = models.ForeignKey('Person', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    complexity = models.OneToOneField(Complexity, on_delete=models.CASCADE)
    type = models.ForeignKey(Spec, on_delete=models.CASCADE)
    tourists = models.ManyToManyField(Tourist, related_name='tours')
