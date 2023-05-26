# 벡터 연산으로 그림 그리기 - GJAI Pre-Training 심화
# 원리는 최대 좌표 값을 정의한 다음 maplotlib의 scatter를 통해 그림을 그린 것이다.
# 좌표값 사이의 랜덤한 좌표를 입력받을 때 마다 다음 함수를 반복한다.
# 내가 원하고자 하는 그림의 좌표일 경우 accpet_points 리스트에 저장한다. 반대일 경우 reject_points 리스트에 저장한다.
# 이후 그림은 다음과 같이 그린다.
# reject_points 의 원소인 좌표들은 lightgray 색상으로 산점도를 표현한다. 크기는 0.1로 매우 작게 한다.
# accept_points. 우리가 그리고자 하는 그림과 일치하는 좌표들은 black 색상으로 산점도를 표현한다. 크기는 1로 다소 크게 한다.
# 따라서 figure로 보았을 때 회색 배경에 검은 그림을 그린 것 처럼 보이게 되는 것이다.

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def circle(P):
    return np.linalg.norm(P) - 1 # 밑의 코드와 동일하게 동작합니다.
    # return np.sqrt(np.sum(P * P)) - 1
    
def diamond(P):
    return np.abs(P[0]) + np.abs(P[1]) - 1
    
def smile(P):
    # 각 점들의 좌표에 대해서 행렬로 위치를 표현해놓음
    # 이후 원을 그린 범위를 반환시킴.
    def left_eye(P):
        eye_pos = P - np.array([-0.5, 0.5])

        # 다음과 같이 반환할 수도 있음
        return np.linalg.norm(eye_pos) - 0.1
        # return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1

    def right_eye(P):
        eye_pos = P - np.array([0.5, 0.5])
        return np.sqrt(np.sum(eye_pos * eye_pos)) - 0.1
    
    def mouth(P):
        if P[1] < 0:
            return np.sqrt(np.sum(P * P)) - 0.7
        else:
            return 1

    return circle(P) * left_eye(P) * right_eye(P) * mouth(P)

# 랜덤하게 부여된 좌표가 내가 그리고자 하는 그림의 범위를 벗어나는지 체크하는 checker 함수.
def checker(P, shape, tolerance):
    return abs(shape(P)) < tolerance

def sample(num_points, xrange, yrange, shape, tolerance):
    accepted_points = []
    rejected_points = []
    
    # 임의의 숫자 P = ([x, y]) 를 생성한다.
    for i in range(num_points):
        x = np.random.random() * (xrange[1] - xrange[0]) + xrange[0]
        y = np.random.random() * (yrange[1] - yrange[0]) + yrange[0]
        P = np.array([x, y])
        
        # 이후 f(P) < threshold 일 때에만 점을 찍는다.
        # 코드상에서는 checker 함수를 통해 tolerance 인자를 한계점으로 정의한다.
        # 랜덤하게 부여된 좌표가 내가 그리고자 하는 그림의 범위를 벗어나지 못하도록 하는 것이다.
        if (checker(P, shape, tolerance)):
            accepted_points.append(P)
        else:
            rejected_points.append(P)
    
    return np.array(accepted_points), np.array(rejected_points)

xrange = [-1.5, 1.5] # X축 범위입니다.
yrange = [-1.5, 1.5] # Y축 범위입니다.

# 각 좌표에 대해 3.0 x 3.0 범위를 지정해 놓고 maplotlib의 scatter를 통해 그림을 그린 것이다.
# reject_points 의 원소인 좌표들은 lightgray 색상으로 산점도를 표현한다. 크기는 0.1로 매우 작게 한다.
# accept_points. 우리가 그리고자 하는 그림과 일치하는 좌표들은 black 색상으로 산점도를 표현한다. 크기는 1로 다소 크게 한다.
# 따라서 figure로 보았을 때 회색 배경에 검은 그림을 그린 것 처럼 보이게 되는 것이다.
accepted_points, rejected_points = sample(
    100000, #  점의 개수를 줄이거나 늘려서 실행해 보세요. 너무 많이 늘리면 시간이 오래 걸리는 것에 주의합니다.
    xrange, 
    yrange, 
    smile, # smile을 circle 이나 diamond 로 바꿔서 실행해 보세요.
    0.005) # Threshold를 0.01이나 0.0001 같은 다른 값으로 변경해 보세요.

plt.figure(figsize=(xrange[1] - xrange[0], yrange[1] - yrange[0]), 
           dpi=150) # 그림이 제대로 로드되지 않는다면 DPI를 줄여보세요.
           
plt.scatter(rejected_points[:, 0], rejected_points[:, 1], c='lightgray', s=0.1)
plt.scatter(accepted_points[:, 0], accepted_points[:, 1], c='black', s=1)

plt.savefig("graph.png")