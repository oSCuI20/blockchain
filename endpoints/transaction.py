#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# ./endpoints/transaction.py
#
import api

@api.route('/transaction/new')
def run(method, path, query, headers, body):
  if method not in ['POST']:
    raise api.HttpMethodNotAllowed('Method ' + method + ' not allowed')

  sender, recipient, amount = (0, None, None)

  try:
    if 'sender' in body and body['sender']:
      sender = int(body['sender'], 16)

    if 'recipient' in body:
      recipient = int(body['recipient'], 16)

    if 'recipient' not in body:
      raise
  except:
    raise api.HttpBadRequest('Bad Request')

  if 'amount' in body:
    amount = body['amount']

  return({ 'Status': 200 }, api.bl.run_transaction(sender, recipient, amount))
