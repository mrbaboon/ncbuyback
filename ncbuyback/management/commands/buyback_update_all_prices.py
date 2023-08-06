from buybackprogram.tasks import update_all_prices
from django.core.management import BaseCommand
from eveuniverse.models import EveMarketPrice
from eveuniverse.providers import esi

from buyback.service import update_tracked_price_history


class Command(BaseCommand):
    help = "Updates market prices for all items"

    def handle(self, *args, **options):
        update_all_prices.delay()
