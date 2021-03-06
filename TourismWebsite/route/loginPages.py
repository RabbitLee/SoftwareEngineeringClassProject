from flask import Blueprint
from flask import request
from flask import jsonify
import sys, os
sys.path.append(os.path.dirname(__file__)+'/../database/')
from database.loginOperate import *

login = Blueprint('login', __name__)
agencyLogin = Blueprint('agencyLogin', __name__)

@login.route('/isUserValid', methods=['POST'])
def login_is_user_valid():
   name = request.form['name']
   password = request.form['password']
   if (isUserValid(name, password) == True):
      return jsonify(isValid=True)
   else:
      return jsonify(isValid=False)

@agencyLogin.route('/isUserValid', methods=['POST'])
def agency_login_is_user_valid():
   name = request.form['name']
   password = request.form['password']
   if(isAgencyValid(name, password) == True):
      return jsonify(isValid=True)
   else:
      return jsonify(isValid=False)