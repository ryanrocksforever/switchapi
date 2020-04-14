# secondrevision
from flask import request
from flask_api import FlaskAPI
import sys
import os
import importlib
import json
import threading
import csv
import subprocess
app = FlaskAPI(__name__)

global running
running = False


sys.path.insert(1, './scripts')


@app.route('/', methods=["GET"])
def api_root():
    return {
        "mom found the poop sock": "uh oh she found the pee drawer too"
    }


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
            #os.system("cd scripts")
            print(command)
            os.system(command)
            oldname = "SwitchAPI/scripts/" + filename[86:]
            goodfilename = filename[86:]
            nename = "C:/Users/ATAM PC 004/Documents/switchapi/SwitchAPI/scripts/testdownload.py_token=AM5MCMUP6F2625MMZ6T475C6TYTCY/" + goodfilename[:-36]
            os.rename(oldname, nename)
        else:
            print("no add")
        if "True" in rmdata:
            print("removing")
            # os.system("cd scripts")
            filename = filename[86:]  # 51
            command = "rmdir " + filename
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
            # noinspection PyUnreachableCode
            filenoext = i[:-3]
            returnlist.update({num: filenoext})

        return returnlist


@app.route('/start', methods=["GET", "POST"])
def start():
    global running
    global p

    if request.method == "POST":
        jsondata = request.data
        print(jsondata)
        filename = jsondata['filename']
        #subprocess.call("ls", cwd="scripts/")
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
        return {'device id': deviceid}

if __name__ == "__main__":
    app.run()

# wifi setup need to install luink is https://github.com/balena-io/wifi-connect/issues/303 run commands there too
