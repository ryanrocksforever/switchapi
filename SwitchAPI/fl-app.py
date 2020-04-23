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
import requests

# from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('rootCA.pem')

app = FlaskAPI(__name__)
CORS(app)
global running
global alreadydone
running = False
alreadydone = False
base_path = Path(__file__).parent
sys.path.insert(1, './scripts')


@app.route('/', methods=["GET"])
def api_root():
    return {
        "mom found the poop sock": "uh oh she found the pee drawer too"
    }


def transform(multilevelDict):
    return {str(key) + "abc": (transform(value) if isinstance(value, dict) else value) for key, value in
            multilevelDict.items()}


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
            url = 'https://fileapiryan-app.herokuapp.com/files'
            myobj = {'download': 'True', 'name': filename}

            xrequest = requests.post(url, data=myobj)
            projpath1 = "./scipts/" + jsondata["filename"] + ".py"
            projdir1 = (base_path / projpath1).resolve()
            open(projdir1, 'wb').write(xrequest.content)
            print(xrequest)

        else:
            print("no add")
        if "True" in rmdata:
            print("removing")

            command = "cd scripts & rm " + filename
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
        a = {}
        a.setdefault("i", [])
        for i in files:
            # num = i[0]

            filenoext = i[:-3]
            # i = "id"
            filenoid = filenoext[1:]
            a["i"].append(filenoid)

        return a


@app.route('/start', methods=["GET", "POST"])
def start():
    global running
    global p
    global alreadydone

    if request.method == "POST":
        print("posted")
        print(running)
        print(alreadydone)
        jsondata = request.data
        if running is not True:
            running = True
            print(running)
            print(jsondata)
            filename = jsondata['filename']
            filename = "i" + filename + ".py"
            # subprocess.call("ls", cwd="scripts/")
            try:
                p = subprocess.Popen(['python', filename], cwd="scripts/")
                print(running)
            except:
                running = False
            print("running")
            print(running)
            alreadydone = True

        if running is not False and alreadydone is not True:
            print("stopping")
            print(jsondata)
            print(running)
            try:
                print(running)
                p.terminate()
                print("stopping")
                running = False
            except:
                print("error")
            running = False
            print("stopping")
        alreadydone = False
        print("already done: " + repr(alreadydone))
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
        start = '{"id": "'
        end = '"}'
        openfile.write(start + jsondata["id"] + end)
        print(repr(jsondata))
        openfile.close()
        userid = jsondata["id"]
        return {'success': userid}

    if request.method == "GET":

        openfile = open("accounts.txt", "r")
        jsonid = openfile.read()
        print(jsonid)
        jsonid = jsonid.replace("'", '"')
        # jsonid = {"id": "poopman"}
        print(jsonid)
        jsonid = json.loads(jsonid)
        print(jsonid)
        # openfile.close()
        if "id" in jsonid.keys():
            userid = jsonid["id"]
        else:
            print("Not present")
            userid = None

        return {'id': userid}


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
