# !/usr/bin/env python
# -*- coding: utf-8 -*-
 
##############################################################
# 
# Copyright (c) 2018 USTC, Inc. All Rights Reserved
# 
##############################################################
# 
# File:    evaluate.py
# Author:  roee
# Date:    2018/03/11 15:32:47
# Brief:
# 
# 
##############################################################

import sys
import time
import math


def time2stamp(t):
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    stamp = int(time.mktime(timeArray))
    return stamp

    
def read_out(out_file):
    fin = open(out_file)
    lines = fin.readlines()
    for i in range(len(lines)):
        if lines[i] == '\n':
            flag = i
            break
    pred = {}
    for line in lines[1:flag]:
        eles = line.strip().split()
        if eles[1] != '0':
            pred[eles[0]] = int(eles[1])
    return pred

def read_input(input_lines):
    args = {}
    class_num = int(input_lines[5].strip())
    args['t_start'] = time2stamp(input_lines[class_num+7].strip())
    args['t_end'] = time2stamp(input_lines[class_num+8].strip())
    args['v_class'] = int(input_lines[5].strip())
    args['v_info'] = [line.strip().split() for line in input_lines[6:class_num+6]]
    return args

def read_test(test_file):
    fin = open(test_file)
    res = {}
    for line in fin:
        eles = line.strip().split()
        fname = eles[1]
        if fname in res:
            res[fname] += 1
        else:
            res[fname] = 1
    return res


if __name__ == '__main__':
    out_file = sys.argv[1] + '/output.txt'
    input_file = sys.argv[1] + '/input.txt'
    test_file = sys.argv[1] + '/test.txt'
    input_lines = open(input_file).readlines()
    pred = read_out(out_file)
    args = read_input(input_lines)
    tru = read_test(test_file)
    N = len(args['v_info'])
    A = 0.0
    B = 0.0
    C = 0.0
    for fname, _, _ in args['v_info']:
        y = tru.get(fname, 0)
        _y = pred.get(fname, 0)
        A += ((y - _y) * (y - _y))
        B += (y * y)
        C += (_y * _y)
    A /= N
    B /= N
    C /= N
    score = 1 - math.sqrt(A) / (math.sqrt(B) + math.sqrt(C))
    print sys.argv[1] + '\tStep 1:' + str(score)

# vim: set expandtab ts=4 sw=4 sts=4 tw=100
