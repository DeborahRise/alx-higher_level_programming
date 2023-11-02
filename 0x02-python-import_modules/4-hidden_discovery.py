#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    result = dir(hidden_4)
    for names in result:
        if names[0:2] != "__":
            print(result)
