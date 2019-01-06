from LoadData import dataset

print(dataset)

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# tail
print(dataset.tail(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())