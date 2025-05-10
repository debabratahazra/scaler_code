#import Decision tree classifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

a = [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
b = ['c', 'b', 'c', 'c', 'b', 'c', 'a', 'a', 'a', 'b']
c = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
d = [1, 1, 0, 1, 1]
e = ['a', 'c', 'b', 'a', 'b']

train = pd.DataFrame({'attr1': a, 'attr2': b, 'tar': c})
test = pd.DataFrame({'attr1': d, 'attr2': e})

#returns a dataframe where the values in 'attr2' are replaced with 'l':0, 'm':1, 'h':2
def str_column_to_int(dataset, column):
    #all the unique values in the the attr2
    lookup = {'a': 0, 'b': 1, 'c': 2}
    dataset = dataset.replace({column: lookup})
    return dataset	
	

train = str_column_to_int(train, 'attr2')
test = str_column_to_int(test, 'attr2')

#initialize the classifier
tree = DecisionTreeClassifier(criterion='entropy', max_depth=3)

#fit the model with the attributes and target of the training data
tree.fit(train[['attr1', 'attr2']], train['tar'])

#predict the target for the observations in the test
pred=tree.predict(test[['attr1', 'attr2']])

print(pred)