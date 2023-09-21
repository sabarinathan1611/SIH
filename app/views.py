from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, current_app, make_response,jsonify
from flask_login import login_required, current_user
import json
from . import db
import os
from flask import current_app as app
from .function  import addlist
from .models import List

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():

    return render_template('index.html')


@views.route('/result', methods=['POST', 'GET'])
@login_required
def result():
    # url = request.form.get('url')
    

    # # phising = False  # Initialize phising as False by default

    # if url:
    #     # Check for similar URLs in the database
    #     similar_url = List.query.filter_by(url=url).first()
    #     print("dbvxvdv",similar_url)
    #     if similar_url:
    #         print("dbvxvdv",similar_url.url)
    #         phising = False  # Initialize phising as False by default
    #     else:

    #         phising = True  # Set phising to True

    # else:
    #     return "Invalid URL"

    return render_template('result.html')

# @views.route('/check_url', methods=['POST','GET'])
# def check_url():
#     # Get the URL from the POST request
#     url = request.form.get('url')
#     print(url)

#     if url:
#         # Check for similar URLs
#         similar_urls = List.query.filter(List.list.ilike(f'%{url}%')).all()

#         if similar_urls:
#             # Return a list of similar URLs
#             similar_urls_list = [url_entry.url for url_entry in similar_urls]
#             print("SI<",similar_urls_list)
#             return jsonify({"message": "Similar URLs found", "similar_urls": similar_urls_list})
#         else:
#             return jsonify({"message": "URL not found in the list"})
            
#     else:
#         return "Invalid URL"
#     return redirect(url_for('views.result'))


@views.route('/add',methods=['POST','GET'])
@login_required
def add():
    try:
            file_path = os.path.join(app.config['EXCEL_FOLDER'], 'addlink.xlsx')  # Use correct case 'EXCEL_FOLDER'
            addlist(file_path)  # Call the data processing function
       

    except Exception as e:
        print("Error occurred:", e)
        db.session.rollback()  # Rollback in case of error    
    return redirect(url_for('views.result'))
