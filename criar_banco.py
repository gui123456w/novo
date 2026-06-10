from gerenciador import database, app
from gerenciador.models import *

from flask_login import login_required
with app.app_context():
    database.create_all()