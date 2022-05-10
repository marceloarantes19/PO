def seq(atual, x):
  n = len(x)
  y = x[0:n]
  z = x[0:n]
  if atual > 0:
    for i in range(0,n):
      y = x[0:n]
      pos = i + atual + 1
      print('atual: ', atual, ' -- i ', i, ' ----> ', pos)
      if pos >= n:
        break
      if y[i] == 0 and y[pos] == 0:
        y[i] = atual
        y[pos] = atual
        #print(y)
        z = seq(atual-1, y)
    return z
  else:
    print('x --> ', x,'\n')
    return x

for n in range(3, 11):
  x = []
  #n = int(input('Digite um número: '))
  print('\n********', n)
  x = [0] * n * 2
  seq(n, x)

