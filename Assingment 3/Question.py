# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:23:24 2019

@author: HomeUser
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')