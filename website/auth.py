from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__) #Set up a Blueprint for our flask application

@auth.route('/add-member',methods=['GET','POST']) #Create a path to the add-members page that can reive both post and get requests
def addMember():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        id = request.form.get('id')
        address = request.form.get('address')
        date = request.form.get('date')
        phone = request.form.get('phone')
        mobile_phone = request.form.get('mobile_phone')
    
        if ' ' not in full_name: #Checking if he entered at least two names (first name and last name)
            flash('Must enter full name (first and last name)', category='error')
        elif len(id) != 9: 
            flash('ID number must consist of 9 digits', category='error')
        elif len(id) == 0 or len(full_name) == 0 or len(address) == 0 or len(phone) == 0 or len(mobile_phone) == 0: #If one of the fields is empty
            flash('All fields must be filled', category='error')
        else:
            flash('Successfully added HMO member',category='success')
            #add user to the database

    return render_template('add_member.html')

@auth.route('/summary') #Create a path to the summary page that can recive get requesrts
def summary():
    return render_template('summary.html')

@auth.route('/card') #Create a path to the card page that can recive get requesrts
def card():
    return render_template('card.html')