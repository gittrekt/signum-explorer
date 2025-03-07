from django.core.management import BaseCommand
from celery import Celery, shared_task

from scan.peers import peer_cmd


class Command(BaseCommand):
    help = "Peers monitor"

    def handle(self, *args, **options):
        peer_cmd.delay()
