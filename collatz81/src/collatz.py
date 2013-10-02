#!/usr/bin/env python3
# Independent set  lab5 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
import random


def parse_args():
    parser = argparse.ArgumentParser(description='Do the google page rank.')
    parser.add_argument('-m', '--method', type=int, choices=[1,2,3], default=1, help="Method to use.")    
    parser.add_argument('-N', '--Number', type=int, default=10, help="Number of sequences to generate.")    
    args = parser.parse_args()
    return args.Number, args.method

def gen_seq(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        seq.append(int(n))        
    return seq

def gen_flattened_seq(N):
    flattened = []
    for n in range(1, N+1):
        if n % 100 == 0:
            print("n {:d}".format(n))
        c_n = gen_seq(n)
        #print("seq #{:d} {:s}".format(n, c_n))
        flattened += c_n

    return flattened

def find_max_in_seq(N):
    max_nbr = 0
    for n in range(1, N+1):
        element = n
        if element > max_nbr:
            max_nbr = element
        while element != 1:
            if element % 2 == 0:
                element /= 2
            else:
                element = element * 3 + 1
            if element > max_nbr:
                max_nbr = element
    return int(max_nbr)


def is_i_in_seq(N, i):
    for n in range(1, N+1):
        element = n
        if element == i:
            return True
        while element != 1:
            if element % 2 == 0:
                element /= 2
            else:
                element = element * 3 + 1
            if element == i:
                return True
    return False

def count_distict(N, max_nbr):
    nbr_distinct = 0
    for i in range(1, max_nbr + 1):
        if is_i_in_seq(N, i):
            nbr_distinct += 1
    return nbr_distinct

        

def calc_algo(C_N):
    freqs = {}
    max_val = 0
    cnt = 0
    for c in C_N:
        if cnt % 100 == 0:
            print("progress: {:f}".format(cnt/len(C_N)))
        cnt += 1
        if c > max_val:
            max_val = c
        if c not in freqs.keys():
            freqs[c] = 0
        freqs[c] += 1
    return max_val, len(freqs.keys()), sum(freqs.values())


        

def main():
    N, method = parse_args()
    if method == 1:
        C_N = gen_flattened_seq(N)
        #print("C_{:d} {:s}".format(N, C_N))
        max_val, nbr_unique, tot_len = calc_algo(C_N)
        print("Max val = {:d}, |C_N| = {:d}, len(C_N) = {:d}".format(max_val, nbr_unique, tot_len))
    elif method == 2:
        max_nbr = find_max_in_seq(N)
        #print("max number in C_{:d} = {:d}".format(N, max_nbr))
        distinct_elems = count_distict(N, max_nbr)
        print("The number of distinct elements was {:d}".format(distinct_elems))


    return 0

if __name__ == '__main__':
    sys.exit(main())
