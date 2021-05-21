#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:42:12 2021

@author: franciscohenriquez
"""



'''
lim_l=[0, 13.5, 30, 50, 70, 90, 120, 310]
lim_u=lim_l[1:]+[math.inf]
tasa=[0, 0.04, 0.08, 0.135, 0.23, 0.304, 0.35, 0.4]

def calc_gc(ing, lim_u, lim_l, tasa):
    if ing<lim_u and ing>=lim_l:
        imp=(ing-lim_l)*tasa
    elif ing>lim_u:
        imp=(lim_u-lim_l)*tasa
    else:
        imp=0
    return(imp)

ing=40
list(map(calc_gc,[ing]*len(lim_l),lim_u, lim_l, tasa))

reduce(lambda a,b:a+b, list(map(calc_gc,[ing]*len(lim_l),lim_u, lim_l, tasa)))
'''

def gc(ing, at):
    from functools import reduce
    uta_at={2020:595476, 2021:612348}
    uta=uta_at.get(at)
   
    if at<=2020:
        lim_l=[0, 13.5, 30, 50, 70, 90, 120]
        tasa=[0, 0.04, 0.08, 0.135, 0.23, 0.304, 0.35]    
    if at>=2021:
        lim_l=[0, 13.5, 30, 50, 70, 90, 120, 310]
        tasa=[0, 0.04, 0.08, 0.135, 0.23, 0.304, 0.35, 0.4]
        
    ing=ing/uta
    lim_u=lim_l[1:]+[float('inf')]
    
    def calc_gc(ing, lim_u, lim_l, tasa):
        if ing>lim_l and ing<=lim_u:
            imp=(ing-lim_l)*tasa
        elif ing>lim_u:
            imp=(lim_u-lim_l)*tasa
        else:
            imp=0
        return(imp)
    
    return(round(reduce(lambda a,b:a+b, list(map(calc_gc,[ing]*len(lim_l),lim_u, lim_l, tasa)))*uta))


I=5e7
gc(I, 2021)

I_l=[1e6, 1e7, 2e7, 3e7, 4e7, 5e7, 6e7, 7e7, 8e7, 9e7, 1e8]


[gc(i,2021) for i in I_l]



