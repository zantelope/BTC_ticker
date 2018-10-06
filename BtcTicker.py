import requests
import json
import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


class BtcObject(object):
  def __init__(self, dictr):
    self.dictr = dictr
    self.time = dictr["time"]["updated"]
    self.price = dictr["bpi"]["USD"]["rate"]



def getPrice():
  r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  test_object = BtcObject(r.json())
  print(test_object.time)
  print(test_object.price)


setInterval(getPrice, 5)
