# 4.Dict:
# 🟦 What is a Dictionary in Python?
#
# A dictionary is a mutable, unordered collection of key–value pairs.
#
# 📌 Key points:
#
# 1.Keys must be unique
# 2.Keys must be immutable (string, number, tuple…)
# 3.Values can be anything (list, dict, set, etc.)
# 4.Items are stored as {key: value}
#
# 1.1 Accessing Values  d[Keyname] or d.get(KeyValue)

d={"ename":"Suresh","Eid":12345,"Esal:":500000}

print("Dict ename access: and value is:",d["ename"])
print("Dict ename access: and value is using get method:",d.get("ename"))

# 1.2 Adding / Updating  d[NewKey]=Value or d.update({"NewKey": 30})

d["EworkLocation"]="HYD"
print("After added one key value pair to the existing dict:,",d.items())
d["EworkLocation"]="BNG"
print("After added one key value pair to the existing dict:,",d.items())
d.update({"Deptno":20})
print("After added one key value pair to the existing dict:,",d.items())
d.update({"EworkLocation":"CHI"})
print("After added one key value pair to the existing dict:,",d.items())


# 1.3 Removing Items   # pop(),popitem() del d[] and clear

d.pop("EworkLocation")
print("After first pop:",d.items())
d.popitem()
print("After second pop using the popitems:",d.items())




# 1.4 How we can iterate Dict

for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)