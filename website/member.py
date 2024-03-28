from flask import Blueprint, render_template, request, flash, redirect
from . import db
from .models import Member, Corona, Vaccination
import re
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


member = Blueprint('member', __name__) #set up a Blueprint for our flask application

@member.route('/get', methods=['GET']) #create a path to the / page that can reive both post and get requests
def members():
    members = Member.query.all()
    return render_template('members.html', all_members=members)#, imgs=imgs)

@member.route('/create', methods=['GET' ,'POST']) #Create a path to the add-members page that can reive both post and get requests
def addMember():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        id = request.form.get('id')
        address = request.form.get('address')
        date = request.form.get('date')
        phone = request.form.get('phone')
        mobile_phone = request.form.get('mobile_phone')
        
        member = Member.query.filter_by(id=id).first() 
        
        if member: #If there is already a member with such an ID in the system
            flash('Member already exists', category='error')
        elif ' ' not in full_name: #Checking if he entered at least two names (first name and last name)
            flash('Must enter full name (first and last name)', category='error')
        elif len(id) != 9 or not id.isdigit(): 
            flash('ID number must consist of 9 digits', category='error')
        elif not re.match(r'^[0-9-]+$', phone):
            flash('A phone number can only contain numbers and the character -', category='error')
        elif not re.match(r'^[0-9-]+$', mobile_phone):
            flash('A mobile-phone number can only contain numbers and the character -', category='error')
        elif 'file' not in request.files:
            flash('No pick uploaded', category='error')
        elif len(id) == 0 or len(full_name) == 0 or len(address) == 0 or len(phone) == 0 or len(mobile_phone) == 0: #If one of the fields is empty
            flash('All fields must be filled', category='error')
        else:
            file = request.files['file']
            if file.filename != '' and file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                img_name = id + '.' + filename.rsplit('.', 1)[1].lower()
                file.save(os.path.join(os.getcwd(), 'website/static/upload', img_name))
                new_member = Member(full_name=full_name, id=id, address=address, date=date, phone=phone, mobile_phone=mobile_phone, img=img_name)
                db.session.add(new_member)

                db.session.commit()

                flash('Successfully added HMO member',category='success')
                return redirect('/member/get') #Redirect the page to the member's page


    return render_template('create.html')

@member.route('/card', methods=['GET', 'POST'])  #Create a path to the card page that can recive get requesrts
def card():
    if request.method == 'GET':
        member_id = request.args.get('id')
        member = Member.query.get(member_id)
        corona = Corona.query.get(member_id)
        first = Vaccination.query.filter_by(member_id=member_id, vaccin_number=1).first()
        second = Vaccination.query.filter_by(member_id=member_id, vaccin_number=2).first()
        third = Vaccination.query.filter_by(member_id=member_id, vaccin_number=3).first()
        forth = Vaccination.query.filter_by(member_id=member_id, vaccin_number=4).first()
        return render_template('card.html', member=member, corona_ditails=corona, first=first, second=second, third=third, forth=forth)
    
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        id = request.form.get('id')
        address = request.form.get('address')
        date = request.form.get('date')
        phone = request.form.get('phone')
        mobile_phone = request.form.get('mobile_phone')

        if ' ' not in full_name: #Checking if he entered at least two names (first name and last name)
            flash('Must enter full name (first and last name)', category='error')
        elif len(id) != 9 or not id.isdigit(): 
            flash('ID number must consist of 9 digits', category='error')
        elif not re.match(r'^[0-9-]+$', phone):
            flash('A phone number can only contain numbers and the character -', category='error')
        elif not re.match(r'^[0-9-]+$', mobile_phone):
            flash('A mobile-phone number can only contain numbers and the character -', category='error')
        elif len(id) == 0 or len(full_name) == 0 or len(address) == 0 or len(phone) == 0 or len(mobile_phone) == 0: #If one of the fields is empty
            flash('Fields full name, id, address, birth date, phone and mobule phone must be filled', category='error')
        else:
            print(id)
            member = Member.query.get(id)
            img_path = member.img
            if 'file' in request.files:
                file = request.files['file']
                if file.filename != '' and file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    previous_img_path = os.path.join(os.getcwd(), 'website/static/upload', member.img)
                    if os.path.exists(previous_img_path):
                        os.remove(previous_img_path)
                    img_name = id + '.' + filename.rsplit('.', 1)[1].lower()
                    file.save(os.path.join(os.getcwd(), 'website/static/upload', img_name))

            corona = Corona.query.get(id)

            if corona:
                for vacc in corona.vaccination:
                    db.session.delete(vacc)
                db.session.delete(corona)
                db.session.commit()
            
            if member:
                db.session.delete(member)
                db.session.commit()
            new_member = Member(full_name=full_name, id=id, address=address, date=date, phone=phone, mobile_phone=mobile_phone, img=img_name)
            db.session.add(new_member)
            db.session.commit()

        
            new_corona = Corona(positive_date=request.form.get('positive_date'), recovery_date=request.form.get('recovery_date'), member_id=id)
            db.session.add(new_corona)

            vaccin = Vaccination(vaccin_date=request.form.get('first_vaccin_date'), vaccin_number=1, manufacturer=request.form.get('first_manufacturer'), member_id=id)
            db.session.add(vaccin)
            vaccin = Vaccination(vaccin_date=request.form.get('second_vaccin_date'), vaccin_number=2, manufacturer=request.form.get('second_manufacturer'), member_id=id)
            db.session.add(vaccin)
            vaccin = Vaccination(vaccin_date=request.form.get('third_vaccin_date'), vaccin_number=3, manufacturer=request.form.get('third_manufacturer'), member_id=id)
            db.session.add(vaccin)
            vaccin = Vaccination(vaccin_date=request.form.get('forth_vaccin_date'), vaccin_number=3, manufacturer=request.form.get('forth_manufacturer'), member_id=id)
            db.session.add(vaccin)
            db.session.commit()
        
            flash('Successfully updated HMO member',category='success')
            return redirect('/member/get') #Redirect the page to the member's page


@member.route('/delete-member', methods=['GET','POST'])
def delete_member():
    member_id = request.args.get('id')
    member = Member.query.get(member_id)
    corona = Corona.query.get(member_id)
    if corona:
        for vaccin in corona.vaccination:
            db.session.delete(vaccin)
        db.session.delete(corona)
    previous_img_path = os.path.join(os.getcwd(), 'website/static/upload', member.img)
    if os.path.exists(previous_img_path):
        os.remove(previous_img_path)
    db.session.delete(member)
    db.session.commit()
    return redirect('/member/get')
