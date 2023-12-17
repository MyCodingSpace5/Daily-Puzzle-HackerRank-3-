sampledataset = [1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,0,0,1,0,0,1,0]
dataset = ["ping","ping2","ping3","ping4","ping4","ping4","ping5","ping6","ping1","ping9","ping10","ping4","ping2","ping3","ping6","ping7","ping8"]
class Neuron:
    def __init__(self, bias, move):
        self.bias = bias
        self.weight = weight
        self.activated = False
        self.move = move
        def activation(self, data, movedataset):
            for i in range(layerdata):
                if(data[i] == bias && movedataset[i] == movedataset[i]):
                    self.weight+=1
                else-if(data[i] == bias && movedataset[i] == movedataset[i]):
                    self.weight-=1    
            
        
class Layer:
    neurons = []
    def __init__(self, neurondata, objective, data):
        neurons = neurondata
        def returnOutputsOfNeurons(self):
            sumBiases = 0
            for Neuron in nerouns:
                    sumBiases += Neuron.bias
            return sumBiases
        def layerActivated(self, data, movedataset):
            for Neuron in neurons:
                Neuron.activate(data, movedataset)
def generateOutput(Layer):
    for i in range(len(dataset)):
        Layer.neurons.append(Neuron(dataset[i],1))
        Layer.neurons.append(Neuron(dataset[i],-1))
    Layer.layerActivated(sampledataset, dataset)
    return Layer.returnOutputsOfNeurons()
        
