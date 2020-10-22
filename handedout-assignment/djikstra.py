# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:28:18 2018

@author: Isaac
"""

import graph_generation
import numpy
import copy

def dijkstra1( successors, other_node ):
    """
    Dijkstra's Algorithm with no breaking when path found

    Parameters
    ----------
    successors : a list of dictionaries, encoding the "successors list"
    other_node : index ( an int ) of the "target" node "t"

    Returns
    -------
    L[ other_node ] : the shortest path length from 1 to other_node

    """
    # to avoid destroying the data structure
    queue = copy.deepcopy( successors )

    # a list of shortest paths
    L = { 0 : 0, }

    # until all nodes have been checked
    while [ n for n in queue if n != {} ]:

        # init min arc
        min_arc = [ 'null', float( 'inf' ) ]

        # cycle visted nodes
        for node in L:

            # filter out none empty nodes, why?
            # empty nodes must be kept to preserve index because SOMEONE!?
            # decided to store a graph in a list ¯\_(ツ)_/¯ ¯\_(ツ)_/¯
            if queue[ node ] != {}:

                # node with the shortest length
                min_exit = min( queue[ node ], key = queue[ node ].get )

                # shortest arc from node
                x = [ min_exit, queue[ node ][ min_exit ] + L[ node ], node  ]

                # if shorter than current min
                if x[ 1 ] < min_arc[ 1 ]:

                    # replace
                    min_arc = x

        # add to visited nodes w/ shortest paths if shorter
        if min_arc[ 0 ] in L:
            L[ min_arc[ 0 ] ] = min( L[ min_arc[ 0 ] ], min_arc[ 1 ] )
        else:
            L[ min_arc[ 0 ] ] = min_arc[ 1 ]

        # remove from queue
        del queue[ min_arc[ 2 ] ][ min_arc[ 0 ] ]

    return L[ other_node ]

if __name__ == "_main_":

    #the successors list for the graph in courswork.pdf
    successors = [{1 : 2, 2 : 5}, {2 : 3}, {3 : 4}, {0 : 21, 1: 8}]

    """we test our algorithm, running it on "successors" for all possible
    target nodes"""
    for other_node in range(1, 4):
        print(dijkstra1(successors, other_node))

    """we supply our implementation 'disjkstra1_stub' to 'generate_timings', together
    with our ID number"""
    graph_ns, graph_ms, times = graph_generation.generate_timings(dijkstra1, 29593476)