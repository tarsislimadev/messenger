from constants import LINE_BREAK

class Response:
  def __init__(self, request) -> None:
    self.status = '200'
    self.headers = [['Content-Type', 'application/json'] ]
    self.request = request

  def getStatusMessage(self, status = '200') -> str:
    if (status == '200'):
      return 'OK'

    return 'ERROR'

  def getFirstLine(self, status = '200') -> str:
    message = self.getStatusMessage(status)
    return f'HTTP/1.1 {status} {message}'

  def getHeaders(self) -> list:
    headers = []

    for header in self.headers:
      headers.append(f'{header[0]}: {header[1]}')

    return headers

  def getBodyString(self) -> str:
    return '{}'

  def getLines(self) -> list:
    lines = []

    lines.append(self.getFirstLine(self.status))

    headers = self.getHeaders()

    if len(headers) > 0:
      lines.extend(headers)

    lines.append('')
    lines.append(self.getBodyString())
    lines.append('')
    lines.append('')

    return lines

  def __str__(self) -> str:
    return LINE_BREAK.join(self.getLines())
