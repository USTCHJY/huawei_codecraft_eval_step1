#!/usr/bin/python
#-*- coding: utf-8 -*-
 
#####################################################
# Copyright (c) 2018 USTC, Inc. All Rights Reserved
#####################################################
# File:    predictor.py
# Author:  roee
# Date:    2018/03/09 23:52:41
# Brief:
#####################################################

import time
import math

T1 = time.time()

def time2stamp(t):
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    stamp = int(time.mktime(timeArray))
    return stamp

def read_input(input_lines):
    args = {}
    class_num = int(input_lines[5].strip())
    args['t_start'] = time2stamp(input_lines[class_num+7].strip())
    args['t_end'] = time2stamp(input_lines[class_num+8].strip())
    args['v_class'] = int(input_lines[5].strip())
    args['v_info'] = [line.strip().split() for line in input_lines[6:class_num+6]]
    return args

def read_train(ecs_lines):
    flavor_info = {}
    for line in ecs_lines:
        eles = line.split()
        uuid = eles[0]
        flavorName = eles[1]
        createTime = time2stamp(eles[2] + ' ' + eles[3])
        if flavorName in flavor_info:
            flavor_info[flavorName].append([uuid, createTime])
        else:
            flavor_info[flavorName] = [[uuid, createTime]]
    return flavor_info

def pred_tru(train, args):
    t_min = 1e11
    t_max = 0
    for f in train:
        for _, stamp in train[f]:
            t_max = stamp if stamp > t_max else t_max
            t_min = stamp if stamp < t_min else t_min
    pred = {}
    for f, _, _ in args['v_info']:
        pr = float(len(train.get(f, []))) * (args['t_end'] - args['t_start']) / (t_max - t_min)
	pred[f] = int(round(pr))
        key = int(round(pr+42-3.5*int(f[6:])))
        if key >= 0:
            pred[f] = key
        else:
            pred[f] /= 2
    return pred             


def print_pred(pred):
    res = []
    num = 0
    for f in pred:
        num += pred[f]
        res.append(' '.join(map(str, [f, pred[f]])))
    return [str(num)] + res


def predict_vm(ecs_lines, input_lines):
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result
    train = read_train(ecs_lines)
    args = read_input(input_lines)
    pred = pred_tru(train, args)
    result += print_pred(pred)
    result += ['']
    return result


# vim: set expandtab ts=4 sw=4 sts=4 tw=100
