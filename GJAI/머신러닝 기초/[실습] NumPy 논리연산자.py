import numpy as np

def main():
    A = get_matrix()
    print(matrix_tutorial(A))

# 아래 코드 보았을 때 input = sys.stdin.readline() 탑재된 상태임.

# 2차원 배열을 입력받아서 np.array() 에 넣어주면 NumPy Matrix가 된다.
def get_matrix():
    mat = []
    [n, m] = [int(x) for x in input().strip().split(" ")]
    
    # n행 동안 반복해서 입력받는다.
    # mat = list(int(x) for x in input().strip().split(" ") for _ in range(n)) 으로 주어도 무관하다.
    for i in range(n):
         row = [int(x) for x in input().strip().split(" ")]
         mat.append(row)
    return np.array(mat)

def matrix_tutorial(A):
    
    # 아래 코드를 완성하세요.
    # 1. B 변수에 A에 대한 전치행렬을 넣어라.
    # 전치행렬(Transpose) 이란 M행 N열의 행렬을 N행 M열로 변환한 행렬을 말한다.
    # 이 때 i행 j열의 원소의 위치는 j행, i열이 된다.
    # NumPy에서 전치행렬로 변환이 필요하다면 np.transpose(Matrix) 메소드를 사용해주면 된다.
    # 또는 Matrix.T 라는 속성을 주어도 된다.
    # B = np.transpose(A)
    B = A.T

    # NumPy에서 찐 선형대수 관련 세부 패키지는 np.linalg 라는 하위패키지에 내장되어 있다.
    # 행렬의 역행렬을 구하기 위해서는 np.linalg.inv(Matrix) 를 사용하면 된다.
    # 역행렬이란 행렬 A가 있을 때 A와 곱하면 단위행렬이 나오는 유일한 행렬 A^-1을 말한다.
    # 단위 행렬은 정방행렬이면서 대각원소가 모두 1이고 나머지 원소는 0인 행렬을 말한다.
    # 따라서 행렬 A 에 대한 역행렬은 유일하며, 역행렬이 없을 수도 있다. 
    # Numpy 에서 행렬의 역행렬은? np.linalg.inv(Matrix) 다.
    # linalg 는 Linear Algebra 의 약어로 추정된다.
    try:
        C = np.linalg.inv(B)
    except:
        # 역행렬이 구해지지 않을 경우 "not invertible" 을 반환한다.
        return "not invertible"

    # np.sum() 의 인자로 matrix가 아닌 조건식을 줄 수도 있다.
    # 참이면 1, 거짓이면 0으로 합산한다.
    return np.sum(C > 0)

    # 추가로 np.dot(Matrix1, Matrix2) 을 통해 행렬곱을 진행할 수 있다.
    

if __name__ == "__main__":
    main()
