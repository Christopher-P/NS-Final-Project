#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:08:48 2018

@author: Chance DeSmet
This program simulates cascading behavior after assigning political beliefs to 
a set of introductory political nodes.
"""
#from igraph import *
import igraph
import time
import csv
import cairo
import math
import graph_tool.all as gt
#import cairocffi as cairo
def assign_views(node_num,view,g,key):
    tracker = 0
    g.vs["ID"] = ["Neutral"]
    g.vs["MAJ"] = ["Neutral"]
    g.vs["SMAJ"] = ["Neutral"]
    g.vs["NMAJ"] = ["Neutral"]
    g.vs["MEDMAJ"] = ["Neutral"]
    g.vs["FMAJ"] = ["Neutral"]
    #print(g.vs[2])
    r = 0
    d = 0
    for u in view:
        if(u == "R"):
            r+=1
        if(u == "D"):
            d+=1
    print("Republican count is ", r, "Democrat count is", d)
    lenn = len(node_num)
    for node in node_num:
        #print("passed through")
        oc = g.vs.find(node_num[tracker]).index
        g.vs[oc][key] = view[tracker]
        #print(g.vs[oc])
        
        tracker += 1
        #print("Assigned ", tracker, "Nodes their initial value out of:", lenn )
    tracker = 0
    #print(g.vs[2])
    return(g)
def cascade(g,key):
    maj_graph = g
    l = 0
    tock = time.time()
    tlen = len(maj_graph.vs)
    for t in maj_graph.vs:
        rep_count = 0
        dem_count = 0
        neut_count = 0
        #print(maj_graph.vs[l]["ID"])
        if(maj_graph.vs[l][key] == "Neutral"):
             near = maj_graph.neighbors(maj_graph.vs[l]["name"], mode = "ALL")  
             #print("near is", near)
             for items in near:
                 if(maj_graph.vs[items][key] == "R"):
                     rep_count+=1
                 if(maj_graph.vs[items][key] == "D"):
                     dem_count+=1
                 if(maj_graph.vs[items][key] == "Neutral"):
                     neut_count+=1
                     
             if(rep_count > dem_count):
                 maj_graph.vs[l]["MAJ"] = "R"
                 #maj_graph.vs[l]["ID"] = "R"
             if(rep_count < dem_count):
                 maj_graph.vs[l]["MAJ"] = "D"
                 #maj_graph.vs[l]["ID"] = "D"
             if(rep_count*.66 > dem_count):
                 maj_graph.vs[l]["SMAJ"] = "R"
             if(rep_count < .66*dem_count):
                 maj_graph.vs[l]["SMAJ"] = "D"
             if((rep_count > dem_count) & (rep_count > neut_count)):
                 maj_graph.vs[l]["NMAJ"] = "R"
             if((rep_count < dem_count) & (dem_count > neut_count)):
                 maj_graph.vs[l]["NMAJ"] = "D"
             if(rep_count*.8 > dem_count):
                 maj_graph.vs[l]["MEDMAJ"] = "R"
             if(rep_count < .8*dem_count):
                 maj_graph.vs[l]["MEDMAJ"] = "D"
             if(rep_count > (dem_count+neut_count)):
                 maj_graph.vs[l]["FMAJ"] = "R"
             if((rep_count+neut_count) < dem_count):
                 maj_graph.vs[l]["FMAJ"] = "D"
        tick = time.time()

        #print("Done with ", l, "nodes out of ", tlen, "total minutes taken: ", (tick-tock)/60)
        l+=1
    #print("Cascade nodes counts are ", rep_count, dem_count, neut_count) 
    return(maj_graph)            
      


def remove_outs(t):
    g = t
    track = 0
    for t in g.vs:
        cons = 1#g.neighbors(g.vs[track], mode = "ALL")
        if(len(cons) < 0):
            #print("Stripping vertex ", track)
            o = 1
            #g.delete_vertices(track)
    track += 1   
    return(g) 
def strip_csv(name, vlist):
    q = open(name, "rt")
    w = csv.reader(q, delimiter=',')
    node_num = []
    view = []
    track = 0
    glist = []
    len2 = 1250
    masterf = open(vlist, "rt")
    master = csv.reader(masterf, delimiter=',')
    for row in master:
        glist.append(row[0])
    for y in w:        
        if(str(y[0]) in glist):        
            node_num.append(y[0])
            if(float(y[1]) > .43):
                view.append('R')
            else:
                view.append('D')
            track += 1
        #print("Checked another set, we now have ", track, "labelled nodes out of about ", len2 )
        
        
    return(node_num, view)
def main():
    g = igraph.Graph.Read("/home/chance/Desktop/small/NetSciGraph_small_stripped.gml", "gml")
    node_num, view = strip_csv("/home/chance/Desktop/small/sent.csv", "/home/chance/Desktop/small/stripped_verts.csv")
    limit = 100
    key = "MAJ"
    #h = g
    t = assign_views(node_num,view,g,key)
    h = t
    niter = 0
    while(niter < limit):        
        h = cascade(t,key)
        niter += 1
    print("cascaded "+str(limit)+" times")
    key = "MAJ___"
    h.write_gml("/home/chance/Desktop/small/gmls/"+key+"_Labelled_graph_"+str(limit)+"_cascades.gml")
    #h = gt.load_graph("/home/chance/Desktop/to_Brian_small/"+key+"_Labelled_graph_3_cascades.gml", fmt = "gml")
    #plots(h, key)

    key = "SMAJ"
    t = assign_views(node_num,view,g,key)
    niter = 0
    while(niter < limit):        
        h = cascade(t,key)
        niter += 1
    print("cascaded "+str(limit)+" times")
    key = "SMAJ__"
    h.write_gml("/home/chance/Desktop/small/gmls/"+key+"_Labelled_graph_"+str(limit)+"_cascades.gml")
    #plots(h, key)

    key = "NMAJ"
    t = assign_views(node_num,view,g,key)
    niter = 0
    while(niter < limit):        
        h = cascade(t,key)
        niter += 1
    print("cascaded "+str(limit)+" times")
    key = "NMAJ__"
    h.write_gml("/home/chance/Desktop/small/gmls/"+key+"_Labelled_graph_"+str(limit)+"_cascades.gml")
    #plots(h, key)

    key = "MEDMAJ"
    t = assign_views(node_num,view,g,key)
    niter = 0
    while(niter < limit):        
        h = cascade(t,key)
        niter += 1
    print("cascaded "+str(limit)+" times")
    key = "MEDMAJ"
    h.write_gml("/home/chance/Desktop/small/gmls/"+key+"_Labelled_graph_"+str(limit)+"_cascades.gml")
    #plots(h, key)

    key = "FMAJ"
    t = assign_views(node_num,view,g,key)
    niter = 0
    while(niter < limit):        
        h = cascade(t,key)
        niter += 1
    print("cascaded "+str(limit)+" times")
    key = "FMAJ__"
    h.write_gml("/home/chance/Desktop/small/gmls/"+key+"_Labelled_graph_"+str(limit)+"_cascades.gml")
    #plots(h, key)
main()
