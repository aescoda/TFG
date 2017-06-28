#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder

g = geocoder.google('Universidad Miguel Hernandez')
print g.latlng
