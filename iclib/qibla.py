# -*- coding: utf-8 -*-
# Copyright (C) 2015 Fikrul Arif
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Qibla direction calculator"""

from . import formula


def direction(lat, lng):
	return formula.qibla(lat, lng)
direction.__doc__ = formula.qibla.__doc__

def direction_dms(lat, lng):
	"""Calculate qibla direction as 3-tuple of degree-minute-second
	
	Degree and arc minute is int, but arc second can be a floating-point number.
	"""
	return _dms(formula.qibla(lat, lng))

def direction_str(lat, lng, prec=0):
	"""Like direction_dms, but formatted as str 'deg° min\' sec\"'
	
	Param:
	lat
	lng
	prec as int - number of decimal places for the arc second
	"""
	d, m, s = direction_dms(lat, lng)
	# negative input might returns wrong result
	return '{}° {}\' {:.{}f}"'.format(d, m, s, prec)

def _dms(deg):
	seconds = deg * 3600
	m, s = divmod(seconds, 60)
	d, m = divmod(m, 60)
	return (int(d), int(m), s)
