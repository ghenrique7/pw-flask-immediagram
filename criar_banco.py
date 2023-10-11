from app_imediagram import __init__, database
from app_imediagram.models import Usuario, Foto

with __init__.app_context():
    database.create_all()
