
paths=list()

def earliest_ancestor(ancestors, starting_node):
    global paths
    #node: [parent, parent, parent]
    a = {}
    for ancestor in ancestors:
        if ancestor[1] not in a.keys():
            a[ancestor[1]] = list()
            a[ancestor[1]].append(ancestor[0])
        else:
            a[ancestor[1]].append(ancestor[0])

    if starting_node not in a.keys():#has no parents
        return -1

    paths=list()#clear out any old results

    recursive_ancestor(a, starting_node)
    #paths now contains results

    # print("PATHS")
    # print(paths)

    #find the path with the most amount of steps taken
    longest = None

    for path in paths:
        if longest is None:
            longest = path
        elif list(path.values() )[0] > list(longest.values() )[0]:
            longest = path

    return list(longest.keys() )[0]
            
def recursive_ancestor(ancestorsDict, starting_node, stepCounter=0):
    global paths
    if starting_node in ancestorsDict.keys():
        parents = ancestorsDict[starting_node]
        # print(ancestorsDict) test_ancestor.py
        # print("recursing on " + str(starting_node) + " got parents " + str(parents))
        # if len(parents) > 1:
        #     print("Recursion branching")
        for parent in parents:
            return recursive_ancestor(ancestorsDict, parent, stepCounter + 1)
    else:
        #we've found the earliest ancestor since there's no parent to current starting_node
        #add the a dict to our paths list, {result, stepCounter}
        # print("found result " + str(starting_node) + " in " + str(stepCounter) + " steps")
        resultDict = {starting_node: stepCounter}
        paths.append(resultDict)