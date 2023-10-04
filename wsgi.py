import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackendAssignment.settings')

# Create the WSGI application
application = get_wsgi_application()
