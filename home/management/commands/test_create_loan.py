from django.core.management.base import BaseCommand
from home.views_crud import createLoan


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        print('======= start create loan =======')
        createLoan()
        print('======= end create loan =======')
