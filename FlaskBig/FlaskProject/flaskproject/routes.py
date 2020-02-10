

import os


from flask import Flask,flash,request,redirect,url_for
from flask.templating import render_template
from flaskproject import app
from flaskproject.models import start,status,stop,restart



@app.route('/tom_server', methods=('GET','POST'))
def tom_server():
    if request.method == 'POST':
        servers_name = request.form['servers'].split(",")
        action_name= request.form['status']

        error = None
        if error is None:
            if action_name == 'status':
                for server_name in servers_name:
                    status(server_name)
                        #server_name = threading.Thread(target=models.status, args=(server_name,))
                        #server_name.start()
            elif action_name == 'start':
                for server_name in servers_name:
                    start(server_name)

            elif action_name =='stop':
                for server_name in servers_name:
                    stop(server_name)

            elif action_name == 'restart':
                for server_name in servers_name:
                    restart(server_name)


                #flash(error, 'error')

    return render_template('tom_server.html')    
