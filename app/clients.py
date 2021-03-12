from app.models import Client

def client_exists(id_):
    client = Client.query.filter_by(id=id_).first()
    if client:
        return True
    else:
        return False