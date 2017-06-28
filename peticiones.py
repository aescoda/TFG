#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder

g = geocoder.google('Av. de la Vega, 15, 28108 Alcobendas, Madrid')
print g.latlng

location = [38.2749014, -0.6842547] 
#address = geocoder.google(location, method='reverse')
#print str(address)

