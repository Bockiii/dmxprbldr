import requests
from bs4 import BeautifulSoup
import random
import json
import time
import pandas as pd
import os.path


def testBridges(bridges,status):
    for bridge in bridges:
        if bridge.get('data-ref'):
            if bridge.get('data-ref') in IGNORED:
                continue
            RESULTS[bridge.get('data-ref')] = {}
            RESULTS[bridge.get('data-ref')]['timestamp'] = TIMEOFRUN
            errormessages = []
            bridgestring = '/?action=display&bridge=' + bridge.get('data-ref') + '&format=html'
            forms = bridge.find_all("form")
            formstrings = []
            for form in forms:
                formstring = ''
                parameters = form.find_all("input")
                for parameter in parameters:
                    if parameter.get('type') == 'number' or parameter.get('type') == 'text':
                        if parameter.has_attr('required'):
                            if parameter.get('placeholder') == '':
                                if parameter.get('value') == '':
                                    errormessages.append(parameter.get('name'))
                                else:
                                    formstring = formstring + '&' + parameter.get('name') + '=' + parameter.get('value')
                            else:
                                formstring = formstring + '&' + parameter.get('name') + '=' + parameter.get('placeholder')
                    if parameter.get('type') == 'checkbox':
                        if parameter.has_attr('checked'):
                            formstring = formstring + '&' + parameter.get('name') + '=on'
                formstrings.append(formstring)
            if not errormessages:
                # getBridge(URL + bridgestring + random.choice(formstrings),bridge.get('data-ref'))
                r = requests.get(URL + bridgestring + random.choice(formstrings))
                with open("./results/" + bridge.get('data-ref') + '-' + status + '.html', 'w') as file:
                    file.write(r.text)
            else:
                with open("./results/" + bridge.get('data-ref') + '-' + status + '.html', 'w') as file:
                    file.write(str(errormessages))
                # RESULTS[bridge.get('data-ref')]['missing'] = errormessages

gitstatus = ["current", "pr"]

for status in gitstatus:
    if status == "current":
        port = "3000"
    elif status == "pr":
        port = "3001"
    URL = "http://localhost:" + port
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    bridges = soup.find_all("section")
    RESULTS = {}
    TIMEOFRUN = int(time.time())
    IGNORED = ['Tester', 'AnimeUltime', 'Demo', 'WeLiveSecurity', 'PresidenciaPT', 'Shanaproject', 'Flickr', 'Wired', 'Facebook', 'FB2', 'Portuguesa', 'Q Play', 'Filter']
    testBridges(bridges,status)
