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
data = [pig1, pig2, pig3, dog1, dog2, dog3]

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

model = LinearSVC()
# data adaptation (data, classes)
model.fit(data, [1,1,1,0,0,0])


mysterious = [[1,1,1],[1,1,0],[1,0,1],[0,1,1]]
classes =[0,1,0,1]
predictions = model.predict(mysterious)

# sum true´s
correct = (predictions == classes).sum()
total = len(classes)
accuracy = correct/total
print('Accuracy is: ', accuracy *100)