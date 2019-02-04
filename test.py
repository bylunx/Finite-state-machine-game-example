#!/bin/env python
#encoding:utf-8
import machine_etat
etat=0
action=0
for i in range(9):
    action=i
    for a in range(8):
        etat=a
        machine_etat.gestion(etat,action)
