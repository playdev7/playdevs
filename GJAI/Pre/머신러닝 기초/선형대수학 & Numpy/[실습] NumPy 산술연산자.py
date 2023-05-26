import numpy as np

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    A = np.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])

    # 아래 코드를 작성하세요.
    # 1로 표준화는 각 원소가 1을 기준으로 할 때 비중을 얼마나 차지하는지 확인할 수 있도록 변환하는 것이다.
    # 원소의 총합이 1이 되도록 표준화가 되려면 모든 원소의 총합을 각 원소에 나눠주면 된다.
    # 총합은 np.sum(Matrix) 를 통해 진행해주면 된다.
    A = A / np.sum(A)
    
    # 분산(Variance) 란 각 변량에다 그들의 평균을 뺀 "편차" 들에 대한 평균이다.
    # 그대로 평균을 내면 언제나 0이 나오므로 편차들을 제곱한 다음 평균을 내준다.
    # 이 분산(Variance) 값은 한 눈에 확인하기 불편하다.
    # 그래서 제곱을 진행하였으니 제곱근(Square Root)으로 풀어준 것을 우리는 "표준편차" 라고 한다. 
    return np.var(A)

if __name__ == "__main__":
    main()
