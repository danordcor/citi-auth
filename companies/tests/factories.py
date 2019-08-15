"""Companies factories."""

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from ..models import Company, Headquarter

fake = Faker()


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence(lambda n: 'company_%d' % n)


class HeadquarterFactory(DjangoModelFactory):
    class Meta:
        model = Headquarter

    name = factory.Sequence(lambda n: 'headquarter_%d' % n)
    address = fake.address()
