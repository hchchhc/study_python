#!usr/bin/env python3
#-*-coding:utf-8-*-

a = [2, 5, 1, 4, 3]
def hc(lyst):
    i = 1
    while i <len(lyst):
        insert = lyst[i]
        j = i - 1
        while j >=0:
            if insert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = insert
        i += 1
    return lyst
print(hc(a))