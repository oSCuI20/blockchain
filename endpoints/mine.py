#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# ./endpoints/mine.py
#
import api

@api.route('/mine')
def run(method, path, query, headers, body):
  if method not in ['GET']:
    raise api.HttpMethodNotAllowed('Method ' + method + ' not allowed')

  return({ 'Status': 200 }, api.bl.run_block())
