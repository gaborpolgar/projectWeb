
from os import sep


def createHtmlFile(headFile, dataFile, footFile, createHtmlFile):

    headFile = open(headFile, encoding="UTF8")
    footFile = open(footFile, encoding="UTF8")
    createHtmlFile = open(createHtmlFile, "w")
    dataFile = open(dataFile, encoding="UTF8")

    for line in headFile.readlines():
        createHtmlFile.write(line)
    createHtmlFile.write("\n")
    for line in dataFile.readlines():
        createHtmlFile.write("<td>"+line.strip()+"</td>\n")
    createHtmlFile.write("\n")
    for line in footFile.readlines():
        createHtmlFile.write(line)

    headFile.close()
    createHtmlFile.close()
    dataFile.close()
    footFile.close()

createHtmlFile("htmlHead.txt", "kavek.txt", "htmlFoot.txt", "project_03.html")
