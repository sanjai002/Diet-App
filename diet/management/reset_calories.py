from django.core.management.base import BaseCommand
from diet.models import FoodLog

class Command(BaseCommand):
    help = 'Reset consumed calories and consumed foods'

    def handle(self, *args, **options):
        try:
            # Your logic to reset consumed calories and consumed foods goes here
            FoodLog.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Successfully reset consumed calories and consumed foods.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error resetting consumed calories and consumed foods: {e}'))
