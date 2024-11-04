"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.


"""

s = "abcde"
goal = "cdeab"


super_S = s+s

if len(s) != len(goal):
    print("False")

if goal in super_S:
    print("true")