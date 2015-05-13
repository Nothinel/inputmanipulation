import re
import sys
if len(sys.argv)>=2:
    inputfilename = sys.argv[1]
else:
    inputfilename = "input.dat"

inputfile = open(inputfilename, 'r')
inhalt = []
oxygen = 0
lithium = 0
niobium = 0
fluency = ""
oxygenden = ""
lithiumden = ""
niobiumden = ""
ionenergy=""
nofit = 0
s2f=""


for i in range(2,len(sys.argv)):
    if re.search("fluency", sys.argv[i]):
        fluency = sys.argv[i+1]
    if re.search("oxyden", sys.argv[i]):
        oxygenden = sys.argv[i+1]
        oxygen = 1
    if re.search("nioden", sys.argv[i]):
        niobiumden = sys.argv[i+1]
    if re.search("lithden", sys.argv[i]):
        lithiumden = sys.argv[i+1]
    if re.search("s2f", sys.argv[i]):
        s2f = sys.argv[i+1]
    if re.search("nofit", sys.argv[i]):
        nofit = 1       
 

for line in inputfile:
    #if re.search(r"([0-9])?(\.)?([0-9].*)?e?\+?[0-9]",line):
     #   print line
    if re.search("ion-energy", line):
        if ionenergy != "":
            line = "      <ion-energy>" + ionenergy + "</ion-energy>\n"
    elif re.search("ion-fluence", line):
        if fluency:
            line = "      <ion-fluence fittable=\"TRUE\">" + fluency + "</ion-fluence>\n"
    elif re.search("<spectrum-to-fit>", line):
        if s2f:
            line = "      <spectrum-to-fit>" + s2f + "</spectrum-to-fit>-->"
        if nofit:
            line = "      <!--<spectrum-to-fit>" + s2f + "</spectrum-to-fit>-->"
            print "HIER BIN ICH"
    elif re.search("Oxygen",line):
        oxygen=1
    elif re.search("Lithium",line):
        lithium=1
    elif re.search("Niobium",line):
        nobium=1

    elif (oxygen == 1) & (oxygenden != ""):
        if re.search("atomic-density fittable", line):
            line = "      <atomic-density fittable=\"FALSE\">" + oxygenden + "</atomic-density>\n"
            oxygen = 0
    elif (niobium == 1) & (niobiumden != ""):
        if re.search("atomic-density fittable", line):
            line = "      <atomic-density fittable=\"FALSE\">" + niobiumden + "</atomic-density>\n"
            niobium = 0
    elif (lithium == 1) & (lithiumden != ""):
        if re.search("atomic-density fittable", line):
            line = "      <atomic-density fittable=\"FALSE\">" + lithiumden + "</atomic-density>"
            lithium = 0
    
    inhalt.append(line)

inputfile.close()
inputfile = open(inputfilename, 'w')
for zeile in inhalt:
    inputfile.write(zeile)

inputfile.close()

