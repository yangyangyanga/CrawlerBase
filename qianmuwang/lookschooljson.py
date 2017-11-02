import json

# path2 = r"D:\pycharm\project13\day03\qianmuwang\test.json"
# jsonData3 = {"name":"sunck凯", "age":18, "hobby":["money","power","girl"], "parames":{"a":1,"b":2}}
# with open(path2, "w") as f:
#     json.dump(jsonData3, f)

with open(r'D:\pycharm\project13\day03\qianmuwang\school.json', 'rb') as f:
    data=json.load(f)
    print(data)
    print(type(data))