import numpy
import graph_generation

def dijkstra1_stub(successors, other_node):
    """
    Stub of Dijkstra's algorithm
    
    Parameters
    ----------
    successors : a list of dictionaries, encoding the "successors list" (seen in the lectures)
    other_node : index (an int) of the "target" node "t"

    Returns
    -------
    L[other_node] : the shortest path length from 1 to other_node
    
    """
    #store in a convenient variable (n) the number of nodes |V| in the graph
    n = len(successors)

    #initialize the set S of nodes currently reached with a shortest path
    S = []
    S.append(0)

    """initialize the data structure L; for any index i, L[i] contains the shortest path length from
    1 to i (if a 1--i path has already been found); we use a dictionary"""
    
    L = dict()
    L[0] = 0

    """initialize the data structure P; for any index i, P[i] contains the precedessor of a
    shortest 1--i path (if it has already been found); we use, again, a dictionary
    NOTE: is this structure really needed if we are only required to output the length
    of a shortest path, rather than a shortest path itself (i.e., a list of arcs)?"""
    P = dict()
    P[0] = '-'

    #the algorithm iterates until all nodes have been reached (i.e., until len(S) = |V|)
    while len(S) < n:

        """initialize appropriate variables to store the pair (v,w) achieving the smallest
        value of L[v] + l_{vw}"""

        min_val = [ "null", float( "inf" )]

        """we have now to loop over all arcs (v,w) in the cut induced by S, checking whether
        L[v] + lvw is smaller than the smallest value thus found, updating, if that is
        the case, our guess on the pair (v,w) minimizing L[v] + l_{vw};
        we can use two nested loops for this:
        * one going over all nodes v in S
        * one over all successors w of v, skipping any nodes w which are in S
        (as, if both v and w are in S, (v,w) is not in the cut induced by S);
        you can use the snippet provided in coursework.pdf to loop over the
        successors of node v in the internal loop"""      
            

        

        """at the end of the two nested loops,
        we should update L, P, and S with the new node just reached     """
            
    return L[other_node]


if __name__ == "__main__":

    #the successors list for the graph in courswork.pdf
    successors = [{1 : 2, 2 : 5}, {2 : 3}, {3 : 4}, {0 : 21, 1: 8}]

    """we test our algorithm, running it on "successors" for all possible
    target nodes"""
    for other_node in range(1, 4):
        print(dijkstra1_stub(successors, other_node))
        
    """we supply our implementation 'disjkstra1_stub' to 'generate_timings', together
    with our ID number"""
    graph_ns, graph_ms, times = graph_generation.generate_timings(dijkstra1_stub, 2707128)
