import sys, json

def pprint(datf):
    data = json.load(datf)
    print( json.dumps(data, indent=3, sort_keys=True) )

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as dataf:
        pprint(dataf)
