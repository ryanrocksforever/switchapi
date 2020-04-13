# secondrevision
from flask import request
from flask_api import FlaskAPI
import sys
import os
import importlib
import json
import threading
import csv

app = FlaskAPI(__name__)

global running
running = False
global thread

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
    global thread

    if request.method == "POST":
        jsondata = request.data
        print(jsondata)
        filename = jsondata['filename']
        filetorun = importlib.import_module(filename)
        thread = threading.Thread(target=filetorun)
        thread.start()
        running = True

        return {'running': running}

    if request.method == "GET":
        return {'running': running}


@app.route('/stop/<filename>', methods=["GET", "POST"])
def stop():
    global running
    global thread
    if request.method == "POST":
        if running is True:
            thread.join()
        running = False

        return {'running': running}

    if request.method == "GET":
        return {'running': running}


@app.route('/account/<id>', methods=["GET", "POST"])
def account(id):
    if request.method == "POST":
        with open('account.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(id)

        return {'success': id}

    if request.method == "GET":
        with open('account.csv', 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                userid = row
        return {'id': row}


if __name__ == "__main__":
    app.run()

# wifi setup need to install luink is https://github.com/balena-io/wifi-connect/issues/303 run commands there too
