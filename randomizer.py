def f1():
    import random as a1
    a2 = open("database.xml", "rb")
    a3 = a2.read()
    a2.close()
    a4 = []
    a5 = 0
    while True:
        a6 = a3.find(b"<text>", a5)
        if a6 == -1:
            break
        a6 += 6
        a7 = a3.find(b"</text>", a6)
        if a7 == -1:
            break
        a4.append(a3[a6:a7])
        a5 = a7 + 7
    if not a4:
        return
    a8 = a1.randrange(len(a4))
    a9 = a4[a8]
    a10 = (
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        b'<rss version="2.0">\n'
        b'<channel>\n'
        b'<item>\n'
        b'<title>' + a9 + b'</title>\n'
        b'</item>\n'
        b'</channel>\n'
        b'</rss>'
    )
    a11 = open("current_tip.xml", "wb")
    a11.write(a10)
    a11.close()
if __name__ == "__main__":
    f1()
