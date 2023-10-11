from app_imediagram import database, __init__
from app_imediagram.models import Usuario, Foto

with __init__.app_context():
    database.create_all()
