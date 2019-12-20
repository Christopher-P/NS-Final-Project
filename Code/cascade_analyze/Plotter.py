#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import graph_tool.all as gt
import numpy as np
import matplotlib
import scipy
import csv
"""
Created on Wed May  2 17:43:57 2018

@author: chance
"""



def it(mdict):
    for files in os.walk(mdict):
        for file in files:
            vector = file
            
            
    for i in vector:
        key = i[0:6]
        cascades = i[len(i)-16: len(i) - 4]
        cascades = cascades.replace("h","")
        cascades = cascades.replace("_","")
        #print(cascades)
        key = key.replace("_","")
        print(i,key)
        #plots(i,key,mdict,cascades)
        facts(i,key, cascades,mdict)
        



def facts(i, key,cascades,mdict):
    #mdict = "/home/chance/Desktop/small/gmls"
    print(mdict, i, key)
    i = mdict + "/" + i
    g = gt.load_graph(i, fmt = "gml")
    #if I want to plot discrpepancies, to this
    '''
    g = gt.GraphView(g, vfilt=gt.label_largest_component(g))
    w = g.new_edge_property("double")
    w.a = np.random.random(len(w.a)) * 42
    ee, x = gt.eigenvector(g, w)
    print(ee)
    gt.graph_draw(g,  vertex_fill_color=x,
                  vertex_size=gt.prop_to_size(x, mi=5, ma=15),
                  vcmap=matplotlib.cm.gist_heat,
                  vorder=x, output="polblogs_eigenvector" + key + ".pdf")
    '''
    #L = gt.laplacian(g, normalized=True)
    #ew, ev = scipy.linalg.eig(L.todense())
    #figure(figsize=(8, 2))
    #scatter(real(ew), imag(ew), c=sqrt(abs(ew)), linewidths=0, alpha=0.6)
    #xlabel(r"$\operatorname{Re}(\lambda)$")
    #ylabel(r"$\operatorname{Im}(\lambda)$")
    #tight_layout()
    #savefig("norm-laplacian-spectrum.pdf")
    
    
    #'''
    s = open(mdict +"_"+ key +  "_" + cascades+ ".csv", "w")
    w = csv.writer(s, delimiter=',')
    w.writerow(["clustering coefficient is ", gt.global_clustering(g)])
    rep_count = dem_count = nut_count = 0
    
    for it in g.vertices():
        if(g.vertex_properties[key][it] == "R"):
            rep_count += 1
        if(g.vertex_properties[key][it] == "D"):
            dem_count += 1
        if(g.vertex_properties[key][it] == "Neutral"):
            nut_count += 1
    w.writerow(["number of republicans is", rep_count])
    w.writerow(["number of democrats is", dem_count])
    w.writerow(["number of neutrals is", nut_count])
    w.writerow(["graph diameter is", gt.pseudo_diameter(g)])
    
    
    
    s.close()
    print("done with facts")


def plots(p,key,mdict,cascade):
    p = mdict + "/"+p
    print("Key is:", key, "p is", p)
    g = gt.load_graph(p, fmt = "gml")
    #g = h
    red_blue_map = {"R":(1,0,0,1),"D":(0,0,1,1),"Neutral":(.4,.6,.8,1)}
    plot_color = g.new_vertex_property('vector<double>') #possibly put gt in here

    g.vertex_properties['plot_color'] = plot_color
    for v in g.vertices():
        #print("key is:", key, "vector is ", v, "Property is:",g.vertex_properties["name"][v] )
        plot_color[v] = red_blue_map[g.vertex_properties[key][v]]
    
    t = gt.Graph()

    for v in g.vertices():
        tv = t.add_vertex()

    reps = t.add_vertex()
    dems = t.add_vertex()
    root = t.add_vertex()
    t.add_edge(root,reps)
    t.add_edge(root,dems)

    #assign clusters based on political affiliation
    for tv in t.vertices():
        if t.vertex_index[tv] < g.num_vertices():
            if g.vertex_properties[key][tv] == 1:
                t.add_edge(reps,tv)
            else:
                t.add_edge(dems,tv)
    tpos = pos = gt.radial_tree_layout(t, t.vertex(t.num_vertices() - 1), weighted=True)
    cts = gt.get_hierarchy_control_points(g, t, tpos)
    pos = g.own_property(tpos)  
    
    gt.graph_draw(g, pos=pos,
              vertex_size=10,
              vertex_color=g.vertex_properties['plot_color'],
              vertex_fill_color=g.vertex_properties['plot_color'],
              edge_control_points=cts,
              vertex_text_position=1,
              vertex_font_size=9,
              #edge_color=g.vertex_properties['plot_color'],
              vertex_anchor=0,
              bg_color=[0,0,0,1],
              output_size=[4024,4024],
              output="graph_"+key+"_"+cascade+"_.png")
    
    
    '''
    print("Plotting ", key, " graph...")
    plot_color = {}
    red_blue_map = {"R":(1,0,0,1),"D":(0,0,1,1), "Neutral":(0,0,0,1)}
    pos = gt.sfdp_layout(g)
    for v in g.vertices():
        plot_color[v] = red_blue_map[g.vertex_properties[key][v]]
    t = gt.Graph()
    #gt.graph_draw(g, pos=pos, vertex_fill_color=g.vertex_properties["plot_color"], output ="/home/chance/Desktop/to_Brian_test/_"+key+"_plotted.png")
    #gt.graphviz_draw(g, pos=pos, vcolor=g.vertex_properties["plot_color"],output="/home/chance/Desktop/to_Brian_test/_"+key+"_plotted.png" )
    #plot = Plot("/home/chance.desmet/NetSciPlot" + mode + ".png", bbox=(1500, 1500), background="white")
    #plot.add(g, bbox=(20, 20, 1000, 1000))
    #plot.save()
    #visual_style = {}
    #layout = g.layout("kk")
    #visual_style["large"] = layout
    #color_dict = {"R": "red", "D": "blue", "Neutral": "grey"}
    #visual_style["vertex_color"] = [color_dict[keys] for keys in g.vs[key]]
    #visual_style["bbox"] = (2000,2000)
    #visual_style["margin"] = 5
    
    #plot(g,"/home/chance/Desktop/to_Brian_test/_"+key+"_plotted.png", **visual_style)
	
    #plot(g, "/home/chance.desmet/NetSciPlot" + mode + ".png", vertex.size=2, 	
    '''
        
        
def main():
    mdict = "/home/chance/Desktop/small/gmls"
    it(mdict)
    
main()