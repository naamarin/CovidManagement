from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) #set up a Blueprint for our flask application

@auth.route('/add-member',methods=['GET','POST']) #create a path to the add-members page that can reive both post and get requests
def addMember():
    return render_template('add_member.html')

@auth.route('/summary') #create a path to the summary page that can recive get requesrts
def summary():
    return render_template('summary.html')

@auth.route('/card') #create a path to the card page that can recive get requesrts
def card():
    return render_template('card.html')