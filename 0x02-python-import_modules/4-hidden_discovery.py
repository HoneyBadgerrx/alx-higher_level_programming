#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i, s in enumerate(dir(hidden_4)):
        if s[0] == '_' and s[1] == '_':
            continue
        print("{}".format(s))
