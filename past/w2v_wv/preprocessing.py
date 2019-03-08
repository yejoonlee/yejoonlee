from yeznable.word2vec import functions_for_w2v
import csv

def pp(list_raw_files, pp_file_name):
    contents = []
    for fileName in list_raw_files:
        raw_file = open("./data/%s.txt" % fileName, 'r')
        text = raw_file.read()
        text = text.split("\n")
        contents += text
        raw_file.close()

    pp_data = []
    for content in contents:
        line = functions_for_w2v.tokenize(content)
        pp_data.append(line)

    pp_file = open("data/%s.csv" % pp_file_name, 'w')
    wr = csv.writer(pp_file)
    for line in pp_data:
        wr.writerow(line)