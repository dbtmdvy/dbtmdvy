f = open("yesterday.txt", 'r')

yesterday_lyric = ""

while 1:
    line = f.readline()
    if not line: break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"

f.close()

n1_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
n2_of_yesterday = yesterday_lyric.count("Yesterday")
n3_of_yesterday = yesterday_lyric.count("Yesterday")

print "Number of A Word 'Yesterday'", n1_of_yesterday
print "Number of A Word 'Yesterday'", n2_of_yesterday
print "Number of A Word 'Yesterday'", n3_of_yesterday
