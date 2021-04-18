#!/usr/bin/env Python3

# app.py

# MAIN MODULE #######

from db import *
from restaurant import *


food = load( 'food' )
printItems( food, "MENU" )

