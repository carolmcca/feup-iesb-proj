import matplotlib.pyplot as plt

X = [0.1+i*0.1 for i in range(50)]
mium_gluc = [0.152*x**-0.461 for x in X]
mium_xil = [0.075*x**-0.438 for x in X]

plt.figure()
plt.plot(X,mium_gluc)
plt.xlabel('X')
plt.ylabel('miu máximo glucose')
plt.title('miu glucose vs X')
plt.axvline(x=0.1, color = 'r', **{'linestyle': 'dashed'})
plt.figure()
plt.title('miu xilose vs X')
plt.plot(X,mium_xil)
plt.xlabel('X')
plt.ylabel('miu máximo xilose')
plt.axvline(x=0.1, color = 'r', **{'linestyle': 'dashed'})