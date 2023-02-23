from constants import LINE_BREAK

class Request:
  def __init__(self, client) -> None:
    if client == None:
      return
    self.chunk = (client.recv(1024).decode('ascii'))

  def getLines(self) -> list:
    return str(self.chunk).split(LINE_BREAK)

  def getFirstLine(self) -> list:
    firstLine = self.getLines()
    return firstLine[0].split(' ')

  def getMethod(self) -> str:
    firstLine = self.getFirstLine()
    return firstLine[0]
  
  def getFullPath(self) -> str:
    firstLine = self.getFirstLine()
    return firstLine[1].split('?', 2)

  def getPath(self) -> str:
    fullpath = self.getFullPath()
    return fullpath[0]

  def getQueries(self) -> dict:
    fullpath = self.getFullPath()
    queries = {}

    for query, i in fullpath[1]:
      queries[i] = str(query)

    return queries

  def getQuery(self, name: str) -> str:
    queries = self.getQueries()

    if name in queries:
      return str(queries[name])

    return ''

  def getHeaders(self) -> list:
    headers = []
    lines = self.getLines()

    for line in lines:
      if line == '':
        break

      headers.append(line.split(': ', 2))

    return headers

  def getBody(self) -> str:
    isBody = False

    for line in self.getLines():
      if isBody:
        return line

      isBody = line == ''

    return ''
