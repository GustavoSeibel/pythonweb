
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/postgres"
app.config['SECRET_KEY'] = "random string"

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


   def __init__(self, address, in_use, responsible, short_host_name, long_host_name, description, external_partner_access, allowed_ports):
      self.address = address
      self.in_use = in_use
      self.responsible = responsible
      self.short_host_name = short_host_name
      self.long_host_name = long_host_name
      self.description = description
      self.external_partner_access = external_partner_access
      self.allowed_ports = allowed_ports

@app.route('/')
def show_all():
   return render_template('show_all.html', iplists = iplists.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['address'] or not request.form['responsible'] or not request.form['allowed_ports']:
         flash('Please enter all the fields', 'error')
      else:
         iplist = iplists(request.form['address'], request.form['in_use'], request.form['responsible'], request.form['short_host_name'], request.form['long_host_name'], request.form['description'], request.form['external_partner_access'], request.form['allowed_ports'])
         
         db.session.add(iplist)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(host = '0.0.0.0', debug = True)
