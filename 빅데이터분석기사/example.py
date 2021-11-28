# https://dataq.goorm.io/exam/116674/%EC%B2%B4%ED%97%98%ED%95%98%EA%B8%B0/quiz/1

# 작업형 1
# 데이터 파일 읽기 예제
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 데이터 불러오기
df = pd.read_csv('data/mtcars.csv', index_col=0)

# 최소최대 척도 변환
scaler = MinMaxScaler()
df[['qsec']] = scaler.fit_transform(df[['qsec']])

# 답안
print(len(df.loc[df.qsec > 0.5]))


# 작업형 2
# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
x_test = pd.read_csv("data/X_test.csv")
x_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")


# 사용자 코딩

# 결과를 위해 cust_id 저장
x_test_id = x_test.loc[:, 'cust_id']

# 모델링을 위한 데이터
x_train = x_train.iloc[:, 1:]
y_train = y_train.iloc[:, -1] # cust_id 제외
x_test = x_test.iloc[:, 1:]

#print(x_train.describe())
#print(y_train.describe())
#print(y_train.dtypes)

# 결측치 확인 및 처리
#print(x_train.isnull().sum())
#print(x_test.isnull().sum())

x_train = x_train.fillna(0) # 또는 x_train['환불금액'] = x_train['환불금액'].fillna(0)
y_train = y_train.fillna(0) # 또는 y_train['환불금액'] = y_train['환불금액'].fillna(0)
x_test = x_test.fillna(0)

#  명목형 변수들을 숫자형 변수로 변환
from sklearn.preprocessing import LabelEncoder
x_train[['주구매상품', '주구매지점']] = x_train[['주구매상품', '주구매지점']].apply(LabelEncoder().fit_transform)
x_test[['주구매상품', '주구매지점']] = x_test[['주구매상품', '주구매지점']].apply(LabelEncoder().fit_transform)

# 분류 모델 생성
# 로지스틱 회귀분석
from sklearn.linear_model import LogisticRegression
 
model = LogisticRegression()
model.fit(x_train, y_train)
print('Logistic socre: ',model.score(x_train, y_train))

# Knn
from sklearn.neighbors import KNeighborsClassifier
 
model = KNeighborsClassifier(n_neighbors=4, metric='euclidean')
model.fit(x_train, y_train)
print('KNN socre: ', model.score(x_train, y_train))

# DT
from sklearn.tree import DecisionTreeClassifier
 
model = DecisionTreeClassifier(random_state=1, max_depth=10)
model.fit(x_train, y_train)
print('DTree score: ', model.score(x_train,y_train))

# RF
from sklearn.ensemble import RandomForestClassifier
 
model = RandomForestClassifier(max_depth=10, n_estimators=100)
model.fit(x_train, y_train)
print('RF score: ', model.score(x_train,y_train))

# SVM
from sklearn.svm import SVC
 
model = SVC(C=10, gamma=1, random_state=1, probability=True)
model.fit(x_train, y_train)
print('SVM socre: ', model.score(x_train,y_train))

# 결과 저장하기
predict = model.predict_proba(x_test)
output = pd.DataFrame({'cust_id':x_test_id, 'gender':predict[:,0]})
# csv로 저장
output.to_csv('1234.csv', index=False)



# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)