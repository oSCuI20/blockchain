# -*- coding: utf-8 -*-
#
# ./exceptions.py
#
class HttpBadRequest(Exception):
  pass


class HttpUnauthorized(Exception):
  pass


class HttpMethodNotAllowed(Exception):
  pass


class HttpNotFoundKey(Exception):
  pass


class HttpNotAllowForMethod(Exception):
  pass


class ServiceUnavailable(Exception):
  pass
