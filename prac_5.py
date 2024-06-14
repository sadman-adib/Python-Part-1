name_dict = {
    "joseph": 3.85,
    "alex": 3.2,
    "john": 3.9,
    "jane": 3.5
}

c = name_dict["john"]
print(c)


print(name_dict["joseph"])
print(name_dict["jane"])


if "john" in name_dict:
  print("john is in name_dict")
if "doe" in name_dict:
  print("doe is in name_dict")

name_dict["doe"] = 3.75

if "john" in name_dict:
  print("john is in name_dict")
if "doe" in name_dict:
  print("doe is in name_dict")

name_dict.pop("john")

if "john" in name_dict:
  print("john is in name_dict")
if "doe" in name_dict:
  print("doe is in name_dict")

print(name_dict)