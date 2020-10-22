# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:22:31 2018

@author: iw1g17
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script that defines a function that can be used as a template for the 
exercise in the script for Computer Lab 7.

Created on Wed Mar 14 18:12:44 2018

"""
import networkx

def print_towns():
    
    
    
    """
    A function to list a series of towns and their distance from Southampton.
    This function can be used as a template for the exercise in the Lab script 7.
    
    This function has no input parameters and does not return any value.

    Created on Wed Mar 14 18:12:44 2018

    """
    H = networkx.Graph()
    H.add_node(1, city = "Southampton")
    node_number = 2
    
    # We create a dictionary of towns and their distances from Southampton
    distances = {
            "London": 79,
            "Reading": 47,
            "Brighton": 69,
            "Exeter": 110,
            "Salisbury": 23,
            "Bath": 64
            }
    for city, distance in distances.items():
        H.add_node(node_number, city=city)
        H.add_edge(1,node_number, distance = distance)
        node_number += 1
        
    
    from matplotlib import pyplot

    pyplot.figure()
    positions = networkx.random_layout(H)
    networkx.draw(H, pos=positions, with_labels=True)
    node_labels = networkx.get_node_attributes(H, "city")
    edge_labels = networkx.get_edge_attributes(H, "distance")
#    networkx.draw_networkx_labels(H, positions, labels=node_labels)
    networkx.draw_networkx_edge_labels(H, positions, edge_labels=edge_labels)
    pyplot.show()
    print(positions)
    
print_towns()   


    



