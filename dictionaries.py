# define an empty dictionary:
d = {}

# define a dictionary with predetermined values:
#d = {"George": 24, "Tom": 32}

# add a key-value pair:
# keys are commonly strings or numbers
d["George"] = 24
d["Tom"] = 16
d["Jenny"] = 16
d[10] = 100


# find a value associated with a key:
print(d["George"])
print(d[10])

# change a value associated with a key:
d["Jenny"] = 20

# how to iterate over key-value pairs?
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")
