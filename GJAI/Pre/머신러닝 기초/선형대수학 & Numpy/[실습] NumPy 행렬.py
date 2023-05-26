import numpy as np

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    # Create the matrix A here...

    # np.array를 통해 NumPy Matrix를 만들 수 있다.
    # Create NumPy Matrix for np.array method.

    # Syntax = np.array([[row0, el1, el2, ...], [row1, el1, el2, ...]])
    A = np.array([[1, 4, 5, 8], [2, 1, 7, 3], [5, 4, 5, 9]])

    # 실제 선형대수의 행렬 곱은 np.dot() 을 사용하여야 한다.
    # matrix * matrix 를 진행하면 각 Element끼리 곱을 한다.
    # 선형대수에서 행렬 곱은 M1 x N1 * M2, N2 일때 N1과 M2의 크기가 같아야 한다.
    # 행렬 곱을 진행하게 되면 M1 x N2 크기의 행렬로 변형된다.
    # 이후 행렬곱의 결과는 다음 예시와 같다
    # 3 x 4 * 4 x 3 행렬일 경우
    # 11은 11*11 + 12*21 + 13*31 + 14*41 12는 11*12 + 12*22 + 13*32 + 14*42 와 같이 되고
    # 33은 31*13 + 32*23 + 33*33 + 34*43 과 같이 구성된다.
    # 잘 안풀리면 손으로 직접 그려가며 풀어보자.
    
    return A

if __name__ == "__main__":
    main()