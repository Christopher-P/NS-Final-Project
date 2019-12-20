#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:31:23 2018

@author: chance

This reads in a graph from the Twitter Data CSV's, then process the important basic properties
"""
import time
import csv
import os
import cairo 
from igraph import *
import matplotlib.pyplot as p
import plotly.plotly as py
import numpy as np
import pylab
import collections
def Read_csvs(name,mdict):
    g = Graph(directed=True)
    #read = csv.reader(open("/home/chance/Desktop/A_stuff/half_data_a.csv", "rt"))
    masterf = open(name, "rt")
    master = csv.reader(masterf, delimiter=',')
    tick = time.time()
    #dictf = open(mdict, "rt")
    #dirc = csv.writer(masterf, delimiter=',')
    #read = csv.reader(open("/home/chance/Desktop/A_stuff/half_data_a.csv", "rt"))
    for row in master:
        #print(row[0])
        intf = row[0]
        #print(g.vs.find(intf))
        g.add_vertex(name = intf)
        #print(g.vs.find(intf))
    tracker = 0
    for files in os.walk(mdict):
        for file in files:
            vector = file                
                
    elist = []
    vlist = []
    nodelist = []
    iterate = 0    
    for item in vector:
        #print(item, len(vector))
        #'''
        #
        #elist = []
        #vlist = []
        p = item
        wd = mdict+str(p)
        #print(wd)
        #print(len(f))
        nscvf = open(wd, "rt")
        ncsv = csv.reader(nscvf, delimiter = ',')
        track = 0
        #print(os.path.exists(wd))        
        print("Nodes added: ", iterate, "0ut of ~1000")
        print("Total time taken is:", time.time()-tick) 
        for rows in ncsv:
            #print(wd)
            #print(os.path.exists(wd))
            if((track > 0)):# & (os.path.exists(wd) == True)):
                #print(rows, wd)                
                i1 = rows[1]
                i2 = rows[2]
                #g.vs.find
                if(i1 == "762354433"):
                    print("Weird one located in i1, ", item)
                if(i2 == "762354433"):
                    print("Weird one located in i2, ", item)
                    print("i2 is ", i2)
                #nodelist.append(i2)
                vlist.append(i2)
                vlist.append(i1)
                nodelist.append(i2)
                #print(vlist)
                elist.append((i1,i2))    
                #g.add_edge(i1,i2)
            track += 1
        #g.add_edges(elist)    
        iterate +=1
        nscvf.close()
        rows = 0
            #'''
    vlist = nodelist
    singles = collections.Counter()
    counter = collections.Counter(vlist)
    print("Entering Counter... ")
    for els in counter:
        if(counter[els] <= 1000):
            #print("els is:", els)
            singles[els] = counter[els]
    glist = list(counter - singles)
    lennew = len(glist)
    print("Length of non pruned list is ", len(vlist))
    print("length of pruned list is ", lennew)
    time.sleep(5)
    #New stuff follows////////////////
    q = open("/home/chance/Desktop/stripped_verts.csv", "w")
    w = csv.writer(q, delimiter=',')
    for it in glist:
        w.writerow([it])
    q.close()
        
    
    #////////////////////////////////////
    #IMPORTANT STUFF UNDER HERE, JUST COMMENTED OUT BECAUSE I NEED ACCES TO THE BASIC VECTOR LIST
    #///////////////////////////////////////////////////////////////////////////////////////////
    vlist = sorted(set(glist))
    lene = len(elist)
    elisto = elist
    elist = []
    track = 0
    count = lene/100
    ocount = count
    percent = 1
    tock = time.time()
    for (t,v) in elisto:
        if(v in vlist):
            elist.append((t,v))
        if(track > count):    
            tick = time.time()
            print("Second time through, done with ", percent, "% of ", lene, "Time taken: ", tick - tock, "there are ", len(elist), "elements in our new list")
            count += ocount
            percent += 1
        track += 1
    #if("762354433" in vlist):
    #    print("it is in there")
    print("Length of vectors is: ", len(vlist))
    
    #cols = open("/home/chance/Desktop/saveverts.csv", "w")
    #colsg = csv.writer(cols, delimiter=',')
    #for elg in colsg
    g.add_vertices(vlist)
    #print(g)
    time.sleep(1)        
    g.add_edges(elist)   
        #g = Graph.TupleList(vertex_name_attr = vlist, edges = elist, directed=False)
    
    return(g)
def strip(g):
    track = 0
    for t in g.vs:
        cons = g.neighbors(g.vs[track], mode = ALL)
        if(len(cons) < 2):
            print("Stripping vertex ", track)
            g.delete_vertices(track)
        track += 1
    return(g)
            

def main():
    #print("5")
    name = "/home/chance/Desktop/A_stuff/half_data_a.csv"
    mdict = "/home/chance/Desktop/A_stuff/half_data_a/"
    i = Read_csvs(name,mdict)
    #i = Graph.Read("/home/chance.desmet/NetSciGraph.gml", "gml")
    i = strip(i)
    print(summary(i))
    i.write_gml("/home/chance/Desktop/NetSciGraph_small_stripped.gml")
    #print(i)
    
main()