from Chap18Tests import test
def flatten(lst):
    """returns a simple list of values from the nested list lst"""
    simple_list = []
    for element in lst:
        if type(element) == type([]):
            simple_list.extend(flatten(element))
        else:
            simple_list.append(element)
    return simple_list

test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])