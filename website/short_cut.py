from flask import Blueprint, redirect

short_cut =  Blueprint('short_cut', __name__) #set up a Blueprint for our flask application

@short_cut.route('/') #Create a path to the summary page that can recive get requesrts
def short_cut1():
    return redirect('/member/get')

@short_cut.route('/member') #Create a path to the summary page that can recive get requesrts
def short_cut2():
    return redirect('/member/get')