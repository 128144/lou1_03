#!/usr/bin/env python3

import sys
import configparser


filename = "test.cfg"
cf = configparser.ConfigParser()
cf.read(filename)
JiShuL = float(cf.get("default","JiShuL"))
JiShuH = float(cf.get("default","JiShuH"))
YangLao = float(cf.get("default","YangLao"))
YiLiao = float(cf.get("default","YiLiao"))
ShiYe = float(cf.get("default","ShiYe"))
GongShang = float(cf.get("default","GongShang"))
ShengYu = float(cf.get("default","ShengYu"))
GongJiJin = float(cf.get("default","GongJiJin"))
SheBaoJiShu = YangLao + YiLiao + ShiYe + GongShang + ShengYu + GongJiJin
def shebao(gongzi):
    if gongzi > JiShuH:
        shebao = JiShuH * SheBaoJiShu
    elif gongzi > JiShuL:
        shebao = gongzi * SheBaoJiShu
    elif gongzi > 0:
        shebao = JiShuL * SheBaoJiShu
    else:
        shebao = 0
    return shebao

alist = ["101,3500\n", "202,5000\n", "309,15000"]
for i in alist:
    gonghao = i.split(",")[0]
    print(gonghao)
    gzje = int(float(i.split(",")[1]))
    print(gzje)
    shebao = shebao(gzje)

#shebao = shebao(gz)
    print(shebao)
print(SheBaoJiShu)
