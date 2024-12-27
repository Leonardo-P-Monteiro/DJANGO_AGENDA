bind = "0.0.0.0:8000"
workers = 3
wsgi_app = "project.wsgi:application" 
# worker_class = "uvicorn.workers.UvicornWorker" # Atenção, pode dar erro aqui pois linha 16 do compose traz essa instrução:     command: gunicorn --config gunicorn/gunicorn.conf.py project.wsgi:application
timeout = 120