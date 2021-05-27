#!/bin/python3




def log(func):
    def inner(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
                                                                                args,
                                                                                kwdargs)
        return str_template + "\n" + str(func(*args, **kwdargs))
    return inner




'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        (a,b,c) = (map(lambda x: float(x.strip()), input().split(',')))
        res_lst.append(average(a,b,c))
        fout.write("{}".format(*res_lst))
