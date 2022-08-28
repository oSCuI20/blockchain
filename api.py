# -*- coding: utf-8 -*-
#
# ./api.py
#
import sys
import json
import http.client

from blockchain import blockchain
from exceptions import (HttpUnauthorized, ServiceUnavailable, HttpMethodNotAllowed,
    HttpNotFoundKey, HttpNotAllowForMethod, HttpBadRequest)

bl = blockchain()

_endpoint = {}

def route(path):
  def inner(fun):
    _endpoint[path] = fun
    return fun
  return inner
#route


def run(method, path, query, headers, body, debug):
  try:
    for q in query:
      if len(query[q]) > 1:
        raise Exception('Multiple values in url')

      query[q] = query[q][0]
    #endfor

    (oheaders, out) = _endpoint[path](method, path, query, headers, body)
    return end(200, out, oheaders, path, debug=debug)

  except HttpBadRequest as e:
    return HttpExceptionHandler(400, e, method, path, query, headers, body, debug)

  except HttpUnauthorized as e:
    return HttpExceptionHandler(401, e, method, path, query, headers, body, debug)

  except HttpNotAllowForMethod as e:
    return HttpExceptionHandler(403, e, method, path, query, headers, body, debug)

  except HttpNotFoundKey or KeyError as e:
    return HttpExceptionHandler(404, e, method, path, query, headers, body, debug)

  except HttpMethodNotAllowed as e:
    return HttpExceptionHandler(405, e, method, path, query, headers, body, debug)

  except Exception as e:
    return HttpExceptionHandler(500, e, method, path, query, headers, body, debug)

  except ServiceUnavailable as e:
    return HttpExceptionHandler(503, e, method, path, query, headers, body, debug)
#run


def HttpExceptionHandler(code, err, method, path, query, headers, body, debug):
  if debug:
    err = {
      'Status': code,
      'reason': {
        'code':    code,
        'err':     str(print_debug(err)),
        'method':  method,
        'path':    path,
        'query':   query,
        'headers': headers,
        'body':    body
      }
    }

  return end(code, err, headers, path, debug)
#HttpExceptionHandler


def end(status =  200, out = '', oheaders = {}, path = '', debug=False):
  if isinstance(out, dict) or isinstance(out, list):
    if debug:    out = json.dumps(out, indent=2)
    else:        out = json.dumps(out)

  h = ''
  for ohead in oheaders.keys():
    if ohead.lower() == 'status':
      h += f'Status: {str(oheaders[ohead])} {http.client.responses[oheaders[ohead]]}\r\n'

    else:
      h += f'{ohead}: {oheaders[ohead]}\r\n'

  h += f'Content-Length: {str(len(out) + 1)}\r\n'

  if 'Content-Type' not in oheaders.keys():
    h += 'Content-Type: application/json; charset=utf-8\r\n'

  h += '\r\n'

  sys.stdout.write(h + out + "\n")
  sys.stdout.flush()

  return status
#end


def print_debug(err):
  return ((f'Error on line {sys.exc_info()[-1].tb_lineno}', type(err).__name__, err))
#print_debug
