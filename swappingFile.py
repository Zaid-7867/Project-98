def swap():
    with open("sample1.txt","r" ) as a:
        dataa=a.read()
    with open("sample2.txt","r" ) as b:
        datab=b.read()
    with open("sample1.txt","w" ) as c:
        c.write(datab)
    with open("sample2.txt","w") as d:
        d.write(dataa)

swap()