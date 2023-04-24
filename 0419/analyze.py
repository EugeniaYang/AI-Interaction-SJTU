#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

def aiui_answer(json_str):
    try:
        dict1 = json_str
        print(type(dict1))
    except:
        dict1 = []
    print(dict1)
    if dict1 and dict1[0]==0:
        print('********')
        if dict1[1] in ["chat","openQA","datetime","weather","calc","baike","idiom"]:
            return dict1[3][0]
        
        elif dict1[1]=="poetry":
            return dict1[3][0]+dict1[3][1]
        
        elif dict1[1]=="news":
            return dict1[3][0]+dict1[3][1]+dict1[3][2]

        else:
            return u"对不起，我不懂这个问题"
    else:
        return u"对不起，我不懂这个问题"
            
