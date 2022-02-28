
def append(list1, list2):
    return list1 + list2
def concat(lists):
    return foldl(append, lists, initial=[])
def filter(function, lst):
    return [item for item in lst if function(item)]
def length(lst):
    count = 0
    for item in lst:
        count += 1
    return count
def map(function, lst):
    return [function(item) for item in lst]
def foldl(function, lst, initial):
    result = initial
    for item in lst:
        result = function(result, item)
    return result
def foldr(function, lst, initial):
    result = initial
    for item in lst[::-1]:
        result = function(item, result)
    return result
def reverse(lst):
    return lst[::-1]
