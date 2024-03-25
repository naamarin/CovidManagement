#the pages
from flask import Blueprint, render_template
from . import db
from .models import Member, Corona, Vaccination

views = Blueprint('views', __name__) #set up a Blueprint for our flask application

@views.route('/',methods=['GET','POST']) #create a path to the / page that can reive both post and get requests
def members():
    members = Member.query.all()
    return render_template('members.html', all_members=members)