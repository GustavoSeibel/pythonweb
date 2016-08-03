from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class iplists(db.Model):
   id = db.Column('ip_id', db.Integer, primary_key = True)
   address = db.Column(db.String(100))
   in_use = db.Column(db.String(10))
   responsible = db.Column(db.String(100))
   short_host_name = db.Column(db.String(100))
   long_host_name = db.Column(db.String(100))
   description = db.Column(db.String(100))
   external_partner_access = db.Column(db.String(100))
   allowed_ports = db.Column(db.String(100))

