from app_imediagram import app, database
from app_imediagram.models import Usuario, Foto

with app.app_context():
    database.create_all()