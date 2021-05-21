#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:42:12 2021

@author: franciscohenriquez
"""



def gc(ing, at):
    
    from functools import reduce
    uta_at={2004:356868, 2005:363696, 2006:378852, 2007:386472, 2008:410664,
            2009:451824, 2010:442356, 2011:451260, 2012:468252, 2013:482472,
            2014:489264, 2015:518376, 2016:539460, 2017:554196, 2018:563664,
            2019:580236, 2020:595476, 2021:612348}
    uta=uta_at.get(at)
    
    if at>=2004 and at<=2013:
        lim_l=[0, 13.5, 30, 50, 70, 90, 120, 150]
        tasa=[0, 0.05, 0.1, 0.15, 0.25, 0.32, 0.37, 0.4] 
    if at>=2014 and at<=2017:
        lim_l=[0, 13.5, 30, 50, 70, 90, 120, 150]
        tasa=[0, 0.04, 0.08, 0.135, 0.23, 0.304, 0.35, 0.4] 
    if at>=2018 and at<=2020:
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

'''
I=190e6
[gc(I, 2021),gc(I, 2021)/I]

I_l=[1e6, 1e7, 2e7, 3e7, 4e7, 5e7, 6e7, 7e7, 8e7, 9e7, 1e8]


[gc(i,2021) for i in I_l]

'''

