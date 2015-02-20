import sys

if len(sys.argv) < 2:
  print('Please provide [inputfile] [outputfile]');

aAscii = 65;
numAnswers = 4;
parsedContents = [];
inFileIndex = 1;
outFileIndex = 2;
inFile = open(sys.argv[inFileIndex])
outFile = open(sys.argv[outFileIndex], 'w');

with inFile as f:
  givenContent = f.readlines();

def toHeaderLine(separator):
  return separator - 6;

def toQuestionLine(separator):
  return separator - 5;

def toAnswerLine(separator, answerI):
  return separator - numAnswers + answerI;

def getAnswerI(headerLine):
  startI = headerLine.find('(', 0); 
  endI = headerLine.find(')', startI);
  answerChar = headerLine[startI + 1 : endI];
  return ord(list(answerChar)[0]) - aAscii;

for i in range(0, len(givenContent)):
  if givenContent[i] == '~~\n':
    headerLine = givenContent[toHeaderLine(i)];
    parsedContents.append(headerLine);
    parsedContents.append(givenContent[toQuestionLine(i)]);
    parsedContents.append(givenContent[toAnswerLine(i, getAnswerI(headerLine))]);
    parsedContents.append('\n');

for line in parsedContents:
  outFile.write("%s" % line)