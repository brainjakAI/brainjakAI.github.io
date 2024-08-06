from pyscript import Element
import requests

# some comment cause i'm testing something :sob:
def check_status():
    url = 'https://brainjakai.xyz'
    status_element = Element("status")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status_element.write("Google is up!")
        else:
            status_element.write("Google is down!")
    except Exception as e:
        status_element.write("Error occurred: " + str(e))

def ping(event):
    check_status()

#pinger button
Element("pingButton").element.addEventListener("click", ping)
