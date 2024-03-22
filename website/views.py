#the pages
from flask import Blueprint, render_template

views = Blueprint('views', __name__) #set up a Blueprint for our flask application

@views.route('/',methods=['GET','POST']) #create a path to the / page that can reive both post and get requests
def members():
    return render_template('members.html')