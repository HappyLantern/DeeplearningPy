
# Image digit classification from MNIST dataset
from keras.datasets import mnist
from keras.utils import to_categorical
from keras import models
from keras import layers
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print(train_images.ndim)
print(train_images.dtype)

# Display input data
digit = train_images[44231]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap = plt.cm.binary)
plt.show()

# Neural network
network = models.Sequential()
network.add(layers.Dense(512, activation = 'relu', input_shape = (28 * 28,)))
network.add(layers.Dense(10, activation = 'softmax'))

network.compile(optimizer = 'rmsprop',
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])

# Preprocessing
# Reshaping/scaling the images to the wanted format and type
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Categorically encoding the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Train network

network.fit(train_images, train_labels, epochs = 20, batch_size = 32)

# Test network

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc', test_acc)
