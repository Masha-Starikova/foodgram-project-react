from csv import DictReader

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Добавляем ингредиенты из файла CSV
    """

    def handle(self, *args, **options):
        for row in DictReader(open('./data/ingredients.csv'), delimiter=";"):
            ingredient = Ingredient(
                name=row['name'], measurement_unit=row['measurement_unit']
            )
            ingredient.save()


    def handle(self, *args, **options):
        with open('./data/ingredients.csv', newline='') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                ingredient = Ingredient(
                    name=row['name'], measurement_unit=row['measurement_unit']
                )
                ingredient.save() 