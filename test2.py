#!usr/bin/env python
#-*-coding:utf-8-*-

import random
import tensorflow as tf
m = tf.constant([2, 3])
print(m)

class hc(object):
    def main(self):

        b = random.randint(0, 99)
        print(b)
        count = 0
        while True:
            count += 1
            a = int(input("input a number \t"))
            if a > b :
                print("大拉")
            elif a < b:
                print("小啦")
            else:
                print("厉害啦",count,'time')
                break


if __name__ == "__main__":
    t = hc()
    t.main()
