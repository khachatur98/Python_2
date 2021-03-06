def max(*args):
    if len(args) == 0:
        print("no numbers given")
        return
    
    max_val = args[0]
    for i in args:
        if i > max_val:
            max_val = i

    return max_val

print(max())
print(max(8, 2, 3, 6, 7))
