from django.core.management import BaseCommand
from scan.peers import peer_cmd_manual


class Command(BaseCommand):
    help = """Peer Monitor Scan
Prints instead of using logging so that the output
can easily be saved to a file such as the following
./manage.py peers_manual > /app/nodes.txt"""

    def handle(self, *args, **options):
        peer_cmd_manual()