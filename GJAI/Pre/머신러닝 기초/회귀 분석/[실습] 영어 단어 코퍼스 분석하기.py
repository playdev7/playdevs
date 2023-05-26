from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# csv 파일 불러오기 위한 csv 모듈 import
import csv

def main():
    words = read_data()

    # lambda 함수를 통해 빈도수를 기준으로 정렬.
    # 그래프로 보았을 때 위에서부터 하강하므로 내림차순 정렬.
    words = sorted(words, key = lambda x : x[1], reverse=True) # words.txt 단어를 빈도수 순으로 정렬합니다.
    
    # 정수로 표현된 단어를 X축 리스트에, 각 단어의 빈도수를 Y축 리스트에 저장합니다.  
    X = list(range(1, len(words)+1))
    Y = [x[1] for x in words]
    
    # X, Y 리스트를 array로 변환합니다. 
    X, Y = np.array(X).reshape(-1,1), np.array(Y)
    
    # X, Y의 각 원소 값에 log()를 적용합니다.
    X, Y = np.log(X), np.log(Y)
    
    # 기울기와 절편을 구한 후 그래프와 차트를 출력합니다. 
    slope, intercept = do_linear_regression(X, Y)
    draw_chart(X, Y, slope, intercept)
    
    return slope, intercept

    Y = [x[1] for x in words]
    
    # X, Y 리스트를 array로 변환합니다. 
    X, Y = np.array(X).reshape(-1,1), np.array(Y)
    
    # X, Y의 각 원소 값에 log()를 적용합니다.
    # X, Y = np.log(X), np.log(Y)
    
    # 기울기와 절편을 구한 후 그래프와 차트를 출력합니다. 
    slope, intercept = do_linear_regression(X, Y)
    draw_chart(X, Y, slope, intercept)
    
    return slope, intercept


# read_data() - words.txt에 저장된 단어와 해당 단어의 빈도수를 리스트형으로 변환합니다.
def read_data():
    # words.txt 에서 단어들를 읽어, 
    # [[단어1, 빈도수], [단어2, 빈도수] ... ]형으로 변환해 리턴합니다.
    
    # csv 모듈의 csv.reader(open()) 을 사용하여 csv를 읽어온다.
    words_csv = csv.reader(open("words.txt"))

    # 데이터 셋이 되어줄 words 리스트이다.
    words = []

    # words_csv 의 각 항목을 words 리스트에 추가시킨다.
    # 변수의 분리는 main 함수에서 다루고 있다.
    for word in words_csv:
            words.append([
                word[0],    # 단어명
                int(word[1])  # 빈도수 실수로
            ])

    return words


# do_linear_regression() - 임포트한 sklearn 패키지의 함수를 이용해 그래프의 기울기와 절편을 구합니다.
def do_linear_regression(X, Y):
    # sklearn - 선형회귀 모델 객체 생성.
    lrmodel = LinearRegression()
    # 해당 모델에 X와 Y 피팅.
    lrmodel.fit(X, Y)

    # sklearn 선형회귀 모델의 기울기는 .coef_ 필드가 담고있다.
    slope = lrmodel.coef_[0]
    # sklearn 선형회귀 모델의 절편은 .intercept_ 필드가 담고있다.
    intercept = lrmodel.intercept_

    return (slope, intercept)

# draw_chart() - matplotlib을 이용해 차트를 설정합니다.
def draw_chart(X, Y, slope, intercept):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.scatter(X, Y)

    # 차트의 X, Y축 범위와 그래프를 설정합니다.
    min_X = min(X)
    max_X = max(X)
    min_Y = min_X * slope + intercept
    max_Y = max_X * slope + intercept
    plt.plot([min_X, max_X], [min_Y, max_Y], 
             color='red',
             linestyle='--',
             linewidth=3.0)
    
    # 기울과와 절편을 이용해 그래프를 차트에 입력합니다.
    ax.text(min_X, min_Y + 0.1, r'$y = %.2lfx + %.2lf$' % (slope, intercept), fontsize=15)
    
    plt.savefig('chart.png')

if __name__ == "__main__":
    main()