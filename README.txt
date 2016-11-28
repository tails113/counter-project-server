--Start Celery--
celery worker -l debug --autoreload -A counter-project --autoscale=10,5 --pidfile=counter-project_celeryd.pid -n counter-project

--Stop Celery--
pkill -f "celery.*counter-project"
