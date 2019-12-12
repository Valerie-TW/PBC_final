from flask import render_template, request, redirect , url_for, Response
from . import blueprint
# import threading,time
from .. import socketio

@blueprint.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST' :

        return render_template("index.html")


@blueprint.route('/page2/<param>',methods=['GET'])
def page1(param):
    
    return render_template("page2.html",param=param)

@blueprint.route('/page1/<param>',methods=["GET"])
def page2(param):
    
    return render_template("page1.html",param=param)