#!/usr/bin/env python

from scipy import constants

print constants.c
print constants.h
print constants.N_A
print constants.physical_constants['electron mass']
print constants.physical_constants

from scipy import special

print special.jn(2, 0.345)