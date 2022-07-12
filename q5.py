def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item

print(list(flatten([[[1, 2, 3], [4, 5]], 6])))

