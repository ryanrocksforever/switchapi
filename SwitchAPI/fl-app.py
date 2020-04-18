# secondrevision
from flask import request
from flask_api import FlaskAPI
import sys
import os
import importlib
import json
import threading
import csv
import re
import subprocess
from flask_cors import CORS

# from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('rootCA.pem')

app = FlaskAPI(__name__)
CORS(app)
global running
running = False

sys.path.insert(1, './scripts')


@app.route('/', methods=["GET"])
def api_root():
    return {
        "mom found the poop sock": "uh oh she found the pee drawer too"
    }

def transform(multilevelDict):
    return {str(key)+"abc" : (transform(value) if isinstance(value, dict) else value) for key, value in multilevelDict.items()}


@app.route('/files', methods=["GET", "POST"])
def files():
    if request.method == "POST":
        print("posting")
        jsondata = request.data

        print(jsondata)
        parseddata = jsondata
        adddata = parseddata['add']
        print("adddata is " + adddata)
        rmdata = parseddata['remove']
        print("rmdata is " + rmdata)
        filename = parseddata["filename"]
        print(repr(filename))
        if "True" in adddata:
            print("adding")
            command = "cd scripts & curl -LJO " + filename
            # os.system("cd scripts")
            print(command)
            os.system(command)
            filename = re.split('API/', filename)
            algoodfile = filename[1]
            goodfile = re.split('_token', algoodfile)
            goodfile = goodfile[0]
            print(filename[1])
            print(goodfile)
            os.rename(algoodfile, goodfile)
        else:
            print("no add")
        if "True" in rmdata:
            print("removing")
            # os.system("cd scripts")
            if filename[0] is "h":
                filename = re.split('API/', filename)
                algoodfile = filename[1]
                goodfile = re.split('_token', algoodfile)
                goodfile = goodfile[0]
                print(filename[1])
                print(goodfile)
            else:

                goodfile = re.split('_token', filename)
                goodfile = goodfile[0]
                print(filename)
                print(goodfile)
            command = "cd scripts & rm " + goodfile
            print(command)
            os.system(command)
        else:
            print("noremove")

        # git.Git("/scripts").clone(filename)
        print("asdfasdf")
        return {'download': "complete"}

    if request.method == "GET":
        print("getting")
        files = os.listdir('./scripts')
        returnlist = {}
        for i in files:

            num = i[0]

            filenoext = i[:-3]
            #i = "id"
            filenoid = filenoext[1:]
            returnlist.update({num: filenoid})


        return returnlist


@app.route('/start', methods=["GET", "POST"])
def start():
    global running
    global p

    if request.method == "POST":
        jsondata = request.data

        print(jsondata)
        filename = jsondata['filename']
        filename = "id"+filename+".py"
        # subprocess.call("ls", cwd="scripts/")
        p = subprocess.Popen(['python', filename], cwd="scripts/")

        global running
        running = True

        return {'running': running}

    if request.method == "GET":
        return {'running': running}


@app.route('/stop', methods=["GET", "POST"])
def stop():
    global running

    if request.method == "POST":
        if running is True:
            p.terminate()
            running = False

        return {'running': running}

    if request.method == "GET":
        return {'running': running}


@app.route('/account', methods=["GET", "POST"])
def account():
    global userid
    if request.method == "POST":

        jsondata = request.data

        openfile = open("accounts.txt", "w")
        openfile.write(repr(jsondata))
        print(repr(jsondata))
        openfile.close()
        userid = jsondata["id"]
        return {'success': jsondata["id"]}

    if request.method == "GET":

        openfile = open("accounts.txt", "r")
        jsonid = openfile.read()
        print(jsonid)
        jsonid = jsonid.replace("'", '"')

        print(jsonid)
        jsonid = json.loads(jsonid)
        print(jsonid)
        openfile.close()
        if "id" in jsonid.keys():
            userid = jsonid["id"]
        else:
            print("Not present")
            userid = None
        if userid is not None:
            return {'id': userid}
        else:
            return {'id': "none"}

@app.route('/acount', methods=["GET", "POST"])
def acount():
    global userid
    if request.method == "POST":

        jsondata = request.data

        openfile = open("accounts.txt", "w")
        openfile.write(repr(jsondata))
        print(repr(jsondata))
        openfile.close()
        userid = jsondata["id"]
        return {'success': jsondata["id"]}

    if request.method == "GET":

        openfile = open("accounts.txt", "r")
        jsonid = openfile.read()
        print(jsonid)
        jsonid = jsonid.replace("'", '"')

        print(jsonid)
        jsonid = json.loads(jsonid)
        print(jsonid)
        openfile.close()
        if "id" in jsonid.keys():
            userid = jsonid["id"]
        else:
            print("Not present")
            userid = None
        if userid is not None:
            return {'id': userid}
        else:
            return {'id': "none"}


@app.route('/device', methods=["GET"])
def device():
    if request.method == "GET":
        openfile = open("device.txt", "r")
        jsonid = openfile.read()
        print(jsonid)
        jsonid = jsonid.replace("'", '"')

        print(jsonid)
        jsonid = json.loads(jsonid)
        print(jsonid)
        deviceid = jsonid["deviceid"]
        openfile.close()
        return {'device_id': deviceid}


if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(host='127.0.0.1', port=80, ssl_context=context, threaded=False, debug=False)

# https://github.com/jasbur/RaspiWiFi
# that is link to wifi setup thing i use
# export FLASK_APP=fl-app.py
# sudo -E flask run --host=switch-hub.local --port=80 --cert=adhoc
# sudo -E flask run --host=switch-hub.local --port=80 --cert=server.crt --key=server.key

# export FLASK_APP=fl-app.py && sudo -E flask run --host=switch-hub.local --port=80 --cert=server.crt --key=server.key