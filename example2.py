#!/usr/bin/python
# -*- coding: utf-8 -*-
from TwitterStream import TwitterStream
import os
import json

oauth_keys = {'consumer_key': <Consumer key>,
              'consumer_secret': <Consumer secret>,
              'access_token_key': <Token key>,
              'access_token_secret': <Token secret>}

post_params = {'include_entities': 0,
               'stall_warning': 'true',
               'track': 'brasil'
               }


def write(path, filename, content=''):
  if not os.path.exists(path):
    os.makedirs(path)
  try:
    with open(path+'/'+filename, 'w') as f: f.write (content)
  except:
    print u'Não foi possível salvar o arquivo %s em %s' % (filename, path)


def handle_tweet(message):
  if message.get('limit'):
      print 'Rate limiting caused us to miss %s tweets' % (message['limit'].get('track'))
  elif message.get('disconnect'):
      raise Exception('Got disconnect: %s' % message['disconnect'].get('reason'))
  elif message.get('warning'):
      print 'Got warning: %s' % message['warning'].get('message')
  else:
      print 'save: %d' % message.get('id')
      write('log/twitter', '%d.json' % message.get('id'), json.dumps(message, indent=True))

if __name__ == '__main__':
    ts = TwitterStream(handle_tweet, oauth_keys, post_params)
    ts.setup_connection()
    ts.start()
