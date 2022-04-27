from sklearn.datasets import load_iris

iris_data = load_iris()
print(type(iris_data))

keys = iris_data.keys()
print('붗꽃 데이터 세트의 키들:', keys)
print('\nfeature_names의 type:', type(iris_data.feature_names))
print('feature_names의 shape:', len(iris_data.feature_names))
print(iris_data.feature_names)

print('\ntarget_names의 type:', type(iris_data.target_names))
print('target_names의 shape:', len(iris_data.target_names))
print(iris_data.target_names)

print('\ndata의 type:', type(iris_data.data))
print('data의 shape:', iris_data.data.shape)
print(iris_data['data'])

print('\ntarget의 type:', type(iris_data.target))
print('target의 shape:', iris_data.target.shape)
print(iris_data.target)