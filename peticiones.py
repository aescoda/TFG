#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder

location = [38.2749014, -0.6842547] 
address = geocoder.google(location, method='reverse')
print address

