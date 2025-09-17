class Sigmoid:
    def forward(self, x):
        self.out = 1 / (1 + np.exp(-x))
        return self.out
    
    def backward(self, grad_out):
        dout = grad_out * (1 - self.out) * self.out
        return dout