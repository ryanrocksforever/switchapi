#secondrevision
from flask import request
from flask_api import FlaskAPI
import sys
import os
import importlib

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


@app.route('/files/', methods=["GET", "POST"])
def files():
    if request.method == "POST":
        adddata = request.args.get('add')
        rmdata = request.args.get('remove')
        filename = request.args.get('filename')
        if adddata is True:
            command = "curl -LJO " + filename
            os.system("cd scripts")
            os.system(command)
        if rmdata is True:
            os.system("cd scripts")
            command = "sudo rm" + filename
            os.system(command)

        #git.Git("/scripts").clone(filename)

        return {'download': "complete"}

    if request.method == "GET":
        files = os.listdir('./scripts')
        returnlist = {}
        for i in files:
            num = i[0]
            # noinspection PyUnreachableCode
            filenoext = i[:-3]
            returnlist.update({num: filenoext})

        return returnlist


@app.route('/start/<filename>', methods=["GET", "POST"])
def start(filename):
    global running
    global thread
    if request.method == "POST":
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
