"""sign-in.py
1. Sign-In Sign-out Logs

Application logs are used in analysis of Interactions with an application and may be used to detect specific actions.

A log file Is provided as a string array where each entry is in the form "user. Id timestamp action". Each of the values Is separated by a space.
• Both user_Id and timestamp consist only of diglts, are at most 9 diglts long and start with a non-zero digit.
• timestamp represents the time in seconds since the application was last launched action will be either "sign-In" or "sign-out"

Given a log with entries in no particular order, return an array of strings that denote user Id's of users who signed out in maxSpan seconds or less aft signing in.


Example
n = 7
logs = ("30 99 sign-In", "30 105 sign-out", "12 100 sign-In", "20 80 sign-In" '12 120 sign-out', "20 101 sign-out", "21 110 sign-in"
maxspan = 20

STDIN 
6 -> logs[] size n = 6
100 10 sign-in
50 20 sign-in
100 15 sign-out
50 26 sign-out
99 2 sign-out


Sample output
99
100

The users with Id's 99 and 100 were not signed in for more than maxspan 5 seconds, In sorted numerical order, the return array Is ("99", "100").
"""
from collections import defaultdict


def logger(logs):
    # Parse the logs into a list
    res = []
    tracker = defaultdict(list)
    for log in logs:
        userid, time, action = log.split(' ')
        tracker[userid].append([time, action])
    for user in tracker:
        tracker[user].sort(key= lambda x: x[0])
        for i in range(len(tracker[user])):
            ...
    print(tracker)






if __name__ == "__main__":
    log1 = ['100 10 sign-in', '50 20 sign-in', '100 15 sign-out', '50 26 sign-out', '99 2 sign-out', "99 1 sign-in",]

    logger(log1)
