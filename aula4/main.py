#features
# long hair? (1 yes, 0 no)
# short leg? (1 yes, 0 no)
# bark? (1 yes , 0 no)

pig1 = [0,1,0]
pig2 = [0,1,1]
pig3 = [1,1,0]

dog1 = [0,1,1]
dog2 = [1,0,1]
dog3 = [1,1,1]

# 1=> pig, 0=> dog
train_x = [pig1, pig2, pig3, dog1, dog2, dog3]
train_y =[1,1,1,0,0,0] # labels
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

model = LinearSVC()
# data adaptation (data, classes)
model.fit(train_x, train_y)
test_x = [[1,1,1],[1,1,0],[1,0,1],[0,1,1]]
test_y =[0,1,0,1]


predictions = model.predict(test_x)
accuracy = accuracy_score(test_y, predictions )
print('accuracy is: %.2f  '% (accuracy *100))