# !/bin/bash
 
##############################################################
# 
# Copyright (c) 2018 USTC, Inc. All Rights Reserved
# 
##############################################################
# 
# File:    eval.sh
# Author:  roee
# Date:    2018/03/11 16:29:27
# Brief:
# 
# 
##############################################################

for eles in `ls`
do
    dir=$eles
    if [ -d $dir ]
    then
		#echo "dir:"$dir
		for eless in `ls $dir`
		do
			ddir="${dir}/"$eless
			#echo ddir:$eless
			if [ -d $ddir ] &&[ $ddir != '.' ];then
				python ecs.py $ddir/train.txt $ddir/input.txt $ddir/output.txt
				python evaluate.py $ddir
			fi
		done
    fi
done

# vim: set expandtab ts=4 sw=4 sts=4 tw=100
