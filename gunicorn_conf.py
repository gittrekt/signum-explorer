# https://docs.gunicorn.org/en/stable/settings.html
import multiprocessing, os
from dotenv import load_dotenv
load_dotenv()

workers = 2 * multiprocessing.cpu_count() - 1
threads = 2 * multiprocessing.cpu_count()
timeout = 60
keepalive = 2
max_requests = 500
max_requests_jitter = 100
worker_tmp_dir = "/dev/shm"
forwarded_allow_ips = "*"
proxy_allow_ips = "*"
loglevel = "info"
daemon = True
pidfile = "/tmp/gunicorn.pid"

if os.environ.get("APP_ASYNC", "off") == "on":
    worker_class = 'config.workers.UvicornWorker'
    bind = "unix:/tmp/gunicorn.sock"
else:
    wsgi_app = "config.wsgi:application"
    bind = "0.0.0.0:5000"