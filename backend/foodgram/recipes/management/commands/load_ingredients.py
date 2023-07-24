import csv
import os
from foodgram import settings

from django.core.management.base import BaseCommand
from progress.bar import IncrementalBar
from recipes.models import Ingredient


def ingredient_create(row):
    Ingredient.objects.get_or_create(
        name=row[0],
        measurement_unit=row[1]
    )


class Command(BaseCommand):
    """Класс добавляет комманду загрузки файла ингридиентов для manage.py.
    Визуализация процесса загрузки через инструмент IncrementalBar."""
    help = "Load ingredients to DB"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'ingredients.csv')
        with open(path, 'r', encoding='utf-8') as file:
            bar = IncrementalBar('ingredients.csv'.ljust(17),
                                 max=len(file.readlines()))
            file.seek(0, 0)
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                bar.next()
                ingredient_create(row)
            bar.finish()
        self.stdout.write("[!] The ingredients has been loaded successfully.")
