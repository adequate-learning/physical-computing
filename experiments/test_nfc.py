import ndef
import nfc
import time
from nfc.clf import RemoteTarget
from threading import Thread

def beam(llc):
    snep_client = nfc.snep.SnepClient(llc)
    snep_client.put_records([ndef.UriRecord('http://nfcpy.org')])

def connected(llc):
    Thread(target=beam, args= (llc,)).start()

try:
  clf = nfc.ContactlessFrontend()
  # FAIL
  # assert clf.open('usb') is True
  #assert clf.open('tty:AMA0') is True

  # ALL WORK
  assert clf.open('tty') is True
  #assert clf.open('tty:S0:pn532') is True
  print(clf)

  # ID=3700A639
  # default bitrate (106A, 106B, 212F)
  #target = clf.sense(RemoteTarget('106A'),RemoteTarget('106B'),RemoteTarget('212F'))
  #print(target)
  #tag = nfc.tag.activate(clf, target)

  def on_connect(tag):
      print(tag.type, tag.identifier.encode("hex").upper())
      print(tag)
      print("tag in on-connect: ", tag)
      print("printing records: ")
      for record in tag.ndef.records:
          print(record)
      return False

  clf.connect(rdwr={'on-connnect': on_connect})
  print("trying to write ndef record to tag:")
  uri, title = 'http://example.com', 'nfc testing'
  record = ndef.SmartposterRecord(uri, title)
  print(record)
  tag.records = [record]
  print(tag.ndef)
  if tag.ndef is not None:
    print(tag.has_changed)


finally:
  clf.close()
