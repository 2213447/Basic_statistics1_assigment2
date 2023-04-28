import numpy as np
import math as math

#dispersion & standard deviation(분산과 표준편차)
def var_std(data, mean):
  S = s = 0
  for i in data:
    S += math.pow(i-mean, 2)
  S /= (len(data) -1)
  s = math.sqrt(S)
  return (S, s)

#Interquartile-Range
def ir(data,p_list):
  k_list = []; q_list = []
  for p in p_list:
    k = (len(data)-1) * p + 1
    k_list.append(k)
  for k in k_list:
    sk = str(k); dot = sk.find('.'); dot_next = sk[dot+1]
    if dot != -1:
      if dot_next == 0:
        q = data[int(k-1)]
        q_list.append(q)
      else:
        q = (data[int(k-1)]+data[int(k)])/2
        q_list.append(q)
  iqr = q_list[-1]-q_list[0]
  print(q_list)
  return iqr

#skewness & kutosis(왜도와 첨도)
def skew(data,mean):
  r = 0
  for i in data:
    r += math.pow((i-mean),3)
  S, s = var_std(data, mean)
  b1 = r / (math.pow(s,3)*(len(data)-1))
  return b1

def kuto(data, mean):
  r = 0
  for i in data:
    r += math.pow((i-mean),4)
  S, s = var_std(data, mean)
  b2 = r / (math.pow(s,4)*(len(data)-1))
  return b2

#Sample covariance & Sample correlation coefficient(공분산, 표본상관계수)
def c_rxy(data1, data2, mean1, mean2):
  sxy = 0
  for i, j in zip(data1, data2):
    rx = (i - mean1); ry = (j - mean2)
    sxy += (rx*ry)
  S1, s1 = var_std(data1, mean1)
  S2, s2 = var_std(data2, mean2)
  c = sxy / (len(data1)-1)
  rxy = c / (s1*s2)
  return (c, rxy)
