#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:42:12 2021

@author: Nestor Gallegos y Francisco Henriquez
"""



def gc(ing, at):
    '''
    ing es la base imponible en pesos 
    at es el anno tributario
    para calcular el gc a una lista, se puede usar [gc(i,at) for i in lista_ing]
    '''
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
    
    '''
    def calc_gc(ing, lim_u, lim_l, tasa):
        if ing>lim_l and ing<=lim_u:
            imp=(ing-lim_l)*tasa
        elif ing>lim_u:
            imp=(lim_u-lim_l)*tasa
        else:
            imp=0
        return(imp)
    '''
    
    def calc_gc(ing, lim_u, lim_l, tasa):
        imp=(min(lim_u, max(ing,lim_l))-lim_l)*tasa
        return(imp)
    
    return(round(reduce(lambda a,b:a+b, list(map(calc_gc,[ing]*len(lim_l),lim_u, lim_l, tasa)))*uta))

'''
I=190e6
[gc(I, 2021),gc(I, 2021)/I]

I_l=[1e6, 1e7, 2e7, 3e7, 4e7, 5e7, 6e7, 7e7, 8e7, 9e7, 1e8]


[gc(i,2021) for i in I_l]

'''

def gc1(ing, at):
    '''
    ing debe ser una variable de un dataframe de pandas
    at es el nno tributario
    '''
    import pandas as pd
    import numpy as np
    #from functools import reduce
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
    

    df_result=pd.DataFrame()
    df_result['base']=ing
    c=0
    df_result['gc_t_tot']=0
    for i in range(len(lim_l)):
        c=c+1
        df_result['gc_t']=np.where(df_result['base']<lim_u[i], (df_result['base']-lim_l[i])*tasa[i],(lim_u[i]-lim_l[i])*tasa[i])
        df_result['gc_t']=np.where(df_result['gc_t']>0, df_result['gc_t'],0)
        df_result['gc_t_tot']=df_result['gc_t_tot']+df_result['gc_t']    
    df_result['gc_t_tot']=round(df_result['gc_t_tot']*uta)
    return(df_result['gc_t_tot'])
