f = open("contents.txt",'r')
txt = f.readlines()

f2 = open("pp_contents.txt",'w')
for l in txt:
    l = l.replace("안녕하세요","")
    l = l.replace("안녕하십니까", "")
    l = l.replace("감사합니다","")
    l = l.replace("궁금합니다", "")
    l = l.replace("부탁드립니다", "")
    l = l.replace("답변", "")
    l = l.replace("조언", "")
    l = l.replace("질문", "")
    l = l.replace("있습니다", "")
    l = l.replace("있어서", "")
    l = l.replace("입니다", "")
    l = l.replace("보통", "")
    l = l.replace("감사합니다", "")
    l = l.replace("관련", "")
    l = l.replace("글을", "")
    l = l.replace("보통", "")

    f2.write(l+'\n')
