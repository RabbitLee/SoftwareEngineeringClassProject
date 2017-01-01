from flask import Blueprint
from flask import request
from flask import jsonify
from database.loginOperate import *

login = Blueprint('login', __name__)


@login.route('/isUserValid', methods=['POST'])
def login_is_user_valid():
   name = request.form['name']
   password = request.form['password']
   if (isUserValid(name, password) == True):
      return jsonify(isValid=True)
   else:
      return jsonify(isValid=False)