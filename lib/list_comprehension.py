#!/usr/bin/env python3

def return_evens(num_list):
    evens= [x for x in num_list if x % 2 ==0]
    return evens
    pass

def make_exclamation(sentence_list):
    exclamation= [n + "!" for n in sentence_list]
    # sentence_list.append("!")
    return exclamation
    pass