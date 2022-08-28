#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# ./endpoints/chain.py
#
import api

@api.route('/chain')
def run(method, path, query, headers, body):
  if method not in ['GET']:
    raise api.HttpMethodNotAllowed('Method ' + method + ' not allowed')

  return({ 'Status': 200 }, { 'chain': api.bl.chain.copy() })
