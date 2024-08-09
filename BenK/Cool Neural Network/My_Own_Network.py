#Importing everything needed
import math
import random
from tensorflow.keras.datasets import mnist
#Setting up the train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#Setting up RELU
def relu(neuron_value):
    if neuron_value > 0:
        return neuron_value
    else:
        return 0
#Setting up the sigmoid function
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
#Setting up weights
def weights(previous_layer):
    temp = []
    for d in range(len(previous_layer)):
        temp.append(sigmoid(random.uniform(-1,1)))
    return temp
#Setting up the neuron setter
def neuron_setter(previous_layer, weights, bias):
    final = 0
    for e in range(len(previous_layer)):
        final += previous_layer[e]*weights[e]
    final += bias
    final = sigmoid(final)
    return final
#Setting up cost function
def cost(final_layer, y_train):
    cost = []
    biggest = 0
    for x in range(0, len(final_layer)):
        if final_layer[biggest] < final_layer[x]:
            biggest = x
    print(final_layer[biggest] ==y_train)
    
    final_cost = 0
    for i in range(len(final_layer)):
        if i == y_train:
            cost.append(((sigmoid(final_layer[i])-1.0)*(sigmoid(final_layer[i])-1.0)))
        else:
            cost.append((sigmoid(final_layer[i])*sigmoid(final_layer[i])))
    for j in range(len(cost)):
        final_cost += cost[j]
    return final_cost
#Setting up the weight changer
def weight_changer(current_layer, previous_layer, current_weights, correct_value):
    wanted_changes = []
    temp = []
    changes = []
    averagingtemp = 0.0
    countertemp = 0.0
    for l in range(len(current_layer)):
        for m in range(len(previous_layer)):
            if l == correct_value:
                temp.append((current_layer[0]-1)*previous_layer[m])
            else:
                temp.append(current_layer[0]*previous_layer[m])
        wanted_changes.append(temp)
        temp = []
    for n in range(len(wanted_changes[0])):
        for o in range(len(wanted_changes)):
            averagingtemp += wanted_changes[o][n]
            countertemp += 1.0
        changes.append(averagingtemp/countertemp)
        averagingtemp = 0.0
        countertemp = 0.0
    for p in range(len(current_weights)):
        current_weights[p]+=changes[p]
    return current_weights
#Setting up the layers
started = False
for a in range(32):
    layer1neurons = []
    for b in range(len(x_train[a])):
        for c in range(len(x_train[a][b])):
            layer1neurons.append(float(x_train[a][b][c])/255)
    if not started:
        layer2weights = weights(layer1neurons)
    print(layer1neurons)
    layer2neurons = []
    for f in range(16):
        layer2neurons.append(neuron_setter(layer1neurons, layer2weights, random.uniform(-1,1)))
    if not started:
        layer3weights = weights(layer2neurons)
    layer3neurons = []
    for g in range(16):
        layer3neurons.append(neuron_setter(layer2neurons, layer3weights, random.uniform(-1,1)))
    if not started:
        layer4weights = weights(layer3neurons)
    layer4neurons = []
    for h in range(10):
        layer4neurons.append(neuron_setter(layer3neurons, layer4weights, random.uniform(-1,1)))
    # print(cost(layer4neurons, y_train[a]))
    layer4weights = weight_changer(layer4neurons, layer3neurons, layer4weights, y_train[a])
    layer3weights = weight_changer(layer3neurons, layer2neurons, layer3weights, y_train[a])
    layer2weights = weight_changer(layer2neurons, layer1neurons, layer2weights, y_train[a])
    started = True
