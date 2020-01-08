import urllib
import base64
import json
import time
import binascii
import os
from hashlib import sha1
import six
import six.moves.urllib as urllib
import hmac

#################################
#                               #
#  CLASSES BUILT FOR GENERATOR  #
#                               #
#################################

name = 'lookerembed'
cred_file = os.path.join(os.path.expanduser('~'),'.creds','creds.json')

with open(cred_file, 'r') as f:
  data = json.loads(f.read())

secret = data['{}'.format(name)]['client_secret']

def to_ascii(s):
  """Compatibility function for converting between Python 2.7 and 3 calls"""
  if isinstance(s, six.text_type):
    return s
  elif isinstance(s, six.binary_type):
    return "".join(map(chr, map(ord, s.decode(encoding='UTF-8'))))
  return s

class Looker:
  def __init__(self, host, secret):
    self.secret = secret
    self.host = host


class User:
  def __init__(self, id=id, first_name=None, last_name=None,
               permissions=[], models=[], group_ids=[], external_group_id=None,
               user_attributes={}, access_filters={}):
    self.external_user_id = json.dumps(id)
    self.first_name = json.dumps(first_name)
    self.last_name = json.dumps(last_name)
    self.permissions = json.dumps(permissions)
    self.models = json.dumps(models)
    self.access_filters = json.dumps(access_filters)
    self.user_attributes = json.dumps(user_attributes)
    self.group_ids = json.dumps(group_ids)
    self.external_group_id = json.dumps(external_group_id)


class URL:
  def __init__(self, looker, user, session_length, embed_url, force_logout_login=False):
    self.looker = looker
    self.user = user
    self.path = '/login/embed/' + urllib.parse.quote_plus(embed_url)
    self.session_length = json.dumps(session_length)
    self.force_logout_login = json.dumps(force_logout_login)

  def set_time(self):
    self.time = json.dumps(int(time.time()))

  def set_nonce(self):
    self.nonce = json.dumps(to_ascii(binascii.hexlify(os.urandom(16))))

  def sign(self):
    #  Do not change the order of these
    string_to_sign = "\n".join([self.looker.host,
                                self.path,
                                self.nonce,
                                self.time,
                                self.session_length,
                                self.user.external_user_id,
                                self.user.permissions,
                                self.user.models,
                                self.user.group_ids,
                                self.user.external_group_id,
                                self.user.user_attributes,
                                self.user.access_filters])

    signer = hmac.new(bytearray(self.looker.secret, 'UTF-8'), string_to_sign.encode('UTF-8'), sha1)
    self.signature = base64.b64encode(signer.digest())

  def to_string(self):
    self.set_time()
    self.set_nonce()
    self.sign()

    params = {'nonce':               self.nonce,
              'time':                self.time,
              'session_length':      self.session_length,
              'external_user_id':    self.user.external_user_id,
              'permissions':         self.user.permissions,
              'models':              self.user.models,
              'group_ids':           self.user.group_ids,
              'external_group_id':   self.user.external_group_id,
              'user_attributes':     self.user.user_attributes,
              'access_filters':      self.user.access_filters,
              'signature':           self.signature,
              'first_name':          self.user.first_name,
              'last_name':           self.user.last_name,
              'force_logout_login':  self.force_logout_login}

    query_string = '&'.join(["%s=%s" % (key, urllib.parse.quote_plus(val)) for key, val in params.items()])

    return "%s%s?%s" % (self.looker.host, self.path, query_string)


# user = User(1,
#               first_name='Embed Wil',
#               last_name='Krouse',
#               permissions=['see_lookml_dashboards', 'access_data', 'see_looks', 'see_user_dashboards'],
#               models=['look_events_project'],
#               group_ids=[1],
#               external_group_id='1',
#               user_attributes={"allowed_brands": "Ray-Ban"}
#               # access_filters={'look_events_project': {'allowed_brands': 'Ray-Ban'}}
#               )

##################################
#                                #
#  GENERATE USER FROM ROUTES.PY  #
#                                #
##################################

def get_user(user_id='1', data={}):
  first_name=data[user_id]['first_name']
  last_name=data[user_id]['last_name']
  permissions=data[user_id]['permissions']
  models=data[user_id]['models']
  group_ids=data[user_id]['group_ids']
  external_group_id=data[user_id]['external_group_id']
  try:
    user_attributes=data[user_id]['user_attributes']
  except:
    user_attributes={'allowed_brands': '%'}

  user = User(user_id,
                first_name=data[user_id]['first_name'],
                last_name=data[user_id]['last_name'],
                permissions=data[user_id]['permissions'],
                models=data[user_id]['models'],
                group_ids=data[user_id]['group_ids'],
                external_group_id=data[user_id]['external_group_id'],
                user_attributes=user_attributes
                # access_filters={'look_events_project': {'allowed_brands': 'Ray-Ban'}}
              )

  return(user)
  

#############################
#                           #
#  URL GENERATOR FUNCTIONS  #
#                           #
#############################

def generate(user):
  looker = Looker('localhost:9999', secret)

  fifteen_minutes = 15 * 60

  url = URL(looker, user, fifteen_minutes, "/embed/dashboards/2", force_logout_login=True)

  # return("https://" + url.to_string() + "?embed_domain=http://localhost:9999")
  return("https://" + url.to_string())




def generate_look(user):
  looker = Looker('localhost:9999', secret)

  fifteen_minutes = 15 * 60

  url = URL(looker, user, fifteen_minutes, "/embed/looks/31", force_logout_login=True)

  # return("https://" + url.to_string() + "?embed_domain=http://localhost:9999")
  return("https://" + url.to_string())


# generate()