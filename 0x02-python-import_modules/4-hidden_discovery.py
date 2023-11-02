#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    result = dir(hidden_4)
    for names in result:
        if names[0:2] != "__":
            print(result)
