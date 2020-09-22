"""
Isopach
Python 3+
Runescape 3 World Pinger
"""

from pythonping import ping
import sys


def worldList():
    f2p = [3, 7, 8, 11, 17, 19, 20, 29, 33, 34, 38, 41, 43,
           55, 57, 61, 80, 81, 94, 101, 120, 122, 135, 136, 141]
           
    p2p = [1,2,4,5,6,9,10,12,14,16,18,21,22,23,24,25,26,27,28,30,31,32,35,36,37,39,40,42,44,45,46,47,48,51,52,53,54,56,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,84,85,86,87,88,89,91,92,96,97,98,99,100,102,103,104,105,106,114,115,116,117,118,119,121,123,124,134,137,138,139,140]

    return f2p, p2p


def pingWorld():
    f2p, p2p = worldList()
    
    print("\nWelcome to Runescape 3 World Pinger by Isopach!")
    print("Please add 'f2p' or 'free' or 'non-members' as argument to ping Non-Members' Worlds.\n")

    try:
        world_type = sys.argv[1]
        if world_type == "f2p" or "free" or "non-members":
            world_type = f2p
        else:
            print("No valid arguments found, defaulting to Members' Worlds...\n")
            world_type = p2p

    except IndexError:
        print("No arguments found, defaulting to Members' Worlds...\n")
        world_type = p2p

    for world_number in world_type:
        server_ping = ping(
            'world' +
            str(world_number) +
            '.runescape.com',
            size=64)
            
        response_list = []
        
        for attr, value in server_ping.__dict__.items():
            response_list.append(value)
            
        res = response_list[0]
        ping_list = []
        
        for i in range(0, len(res)):
            ping_list.append(float(str(res[i]).split(' ')[-1].split('ms')[0]))

        print("World " + str(world_number) + ": " +
              str(int(mean(ping_list))) + "ms")

    return True


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


if __name__ == '__main__':
    pingWorld()
