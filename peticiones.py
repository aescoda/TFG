#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder

g = geocoder.google('Av. de la Vega, 15, 28108 Alcobendas, Madrid')
print g.latlng

location = [40.5339195, -3.6312006] 
address = geocoder.google(location, method='reverse')
print "Las coordenadas especificadas corresponden a:"
print str(address)

