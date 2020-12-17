
# w =  open("text.txt","w",encoding="utf8")
# w.write("qwrasdz\n nasdfa")
# w.close()
# print(w)

with open("text.txt","r",encoding="utf-8") as f:
    result = f.read()
    print(result)

