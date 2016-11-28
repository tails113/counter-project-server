--Start Celery--
celery worker -l debug --autoreload -Ofair -A counter-project --autoscale=10,5 --pidfile=counter-project_celeryd.pid -n counter-project
