code = ['', '', '', '', '', '', '', '', '', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ';', "'", ',', '.', '/', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', '_', '+', '{', '|', ':', '"', '<', '>', '?', '}', ')', ']']

class text:
  def encode(text):
    t = ''
    for i in range(len(text)):
      t = t+str(code.index(text[i])+1)
    return t

  def decode(text):
    t = ''
    try:
      x = 0
      for i in range(int(len(text)/2)):
        t = t+str(code[int(text[x]+text[x+1])-1])
        x =  x + 2
      return t
    except ValueError:
      pass