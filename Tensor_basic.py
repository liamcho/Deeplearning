#Tensor은 Numpy의 배열과 유사, n차원의 행렬로 표현.
#스칼라는 0차원, 벡터는 1차원, 매트릭스는 2차원 Tensor라고 할 수 있다. 주로 5차원까지 사용한다. (Rank)

import numpy as np
import torch


#----------------------------------------------------------------


# torch.tensor() : 기본적으로 tensor를 만드는 방법
a = torch.tensor(5)
b = torch.tensor([ 1,2,3,4,5 ])
c = torch.tensor([ [1],[2],[3],[4],[5] ])
d = torch.tensor([ [1,2,3], [4,5,6], [7,8,9]])

print(a)
print(b)
print(c)
print(d)


temp_set = (1,2,3,4,5)
e = torch.tensor(temp_set)
print(e)


temp_list = [1,2,3,4,5]

temp_np_array = np.array(temp_list)
temp_np_array
print(type(temp_np_array))



#----------------------------------------------------------------



# torch.ones() : 각 엘리먼트가 1인 tensor를 만들어줌 , [ 차원 , 행, 열 ]
# argument로는 tensor의 dimension을 입력

f = torch.ones(3) # 1x3행렬
print(f)

h = torch.ones([3,3]) #3x3행렬
print(h)

i = torch.ones([3,3,3]) #위의 행렬이 3개 , [ 차원 , 행, 열 ]
print(i)




#----------------------------------------------------------------




# torch.zeros() :  각 엘리먼트가 0인 tensor를 만들어줌 (Zero padding) , [ 차원 , 행, 열 ]

f = torch.zeros(3) # 1x3행렬
print(f)

h = torch.zeros([3,3]) #3x3행렬
print(h)

i = torch.zeros([3,3,3]) #위의 행렬이 3개  , [ 차원 , 행, 열 ]
print(i)




#----------------------------------------------------------------




# torch.arange() : 주어진 범위 내의 정수를 순서대로 생성
#                  >> Sequence를 만들어주는 funtion


f = torch.arange(1,10)
print(f)

h = torch.arange(22,10,-2) #22에서 시작 10에서 끝, 2씩 작아짐
print(h)

h = torch.arange(10, 22, 2) 
print(h)





#----------------------------------------------------------------




# torch.rand() : [0, 1]의 균일한 dist에서 난수를 생성해서 tensor으로 만들어줌

f = torch.rand(5)  # 난수 5개 생성 tensor([0.1979, 0.7051, 0.0411, 0.9031, 0.9365])
print(f)

f = torch.rand(5,5)
print(f)

f = torch.rand(5,5,5)
print(f)




#----------------------------------------------------------------




# torch.xxx_like() : 기존의 텐서와 같은 모양의 원소가 @인 텐서 생성
#                     >> 기존의 텐서와 똑같은 모양을 만드는 것.

a = torch.tensor([3,4,5])  
print(a)                   # >> tensor([3, 4, 5])


b = torch.ones_like(a)
print(b)                   # >> tensor([1, 1, 1])


c = torch.zeros_like(a)
print(c)                   # >> tensor([0, 0, 0])



## torch.zeros(), torch.ones()도 된다.

a = torch.zeros([3,4,5]) #0으로 구성된 4행5열 행렬이 3개 만들어짐
print(a)
b = torch.ones_like(a)   #1으로 구성된 4행5열 행렬이 3개 만들어짐
print(b)


# torch.rand()도 된다.

a = torch.rand([3,4,5])
print(a)
b = torch.ones_like(a)
print(b)
