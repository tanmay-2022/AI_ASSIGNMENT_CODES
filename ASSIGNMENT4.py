MIN,MAX= -1000,1000

class MINMAX:

  def maxfun(self, depth, index, values, alpha, beta):
    best = MIN

    for i in range (0,2):
      val = self.minmax(depth+1, index*2 +i, False, values, alpha, beta)
      best= max(val,best)
      alpha=max(best,alpha)

      if beta<=alpha:
        break
    
    return best


  def minfun(self, depth, index, values, alpha, beta):
    best = MAX

    for i in range (0,2):
      val = self.minmax(depth+1, index*2 +i, True, values, alpha, beta)
      best= min(val,best)
      beta=min(best,beta)

      if beta<=alpha:
        break

    return best

  def minmax(self, depth, index, maxplayer, values, alpha, beta):

    if depth==3:
      return values[index]

    if maxplayer:
      best = self.maxfun(depth, index, values, alpha, beta)
      return best
    else:
      best = self.minfun(depth, index, values, alpha, beta)
      return best


 



m=MINMAX()
values = [3, 5, 6, 9, 1, 2, 0, -1] 
print(m.minmax(0,0,True,values,MIN, MAX))