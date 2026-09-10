import matplotlib.pyplot as plt
import numpy as np
name = "5m_vs_6m"
x0 = np.load("./result/qmix/"+name+"/win_rates_0_1.npy")
x8 = np.load("./result/qmix/"+name+"/win_rates_0.npy")
x1 = np.load("./result/qmix/"+name+"/win_rates_1.npy")
x2 = np.load("./result/qmix/"+name+"/win_rates_2.npy")
x3 = np.load("./result/qmix/"+name+"/win_rates_3.npy")
x4 = np.load("./result/qmix/"+name+"/win_rates_4.npy")
x5 = np.load("./result/qmix/"+name+"/win_rates_5.npy")
x6 = np.load("./result/qmix/"+name+"/win_rates_6.npy")
x7 = np.load("./result/qmix/"+name+"/win_rates_7.npy")
x = [x0,x4,x5]
min_len = min([len(i) for i in x])
print([len(i) for i in x])
clipx = [i[:min_len] for i in x]
# for i in range(len(x)):
#     plt.plot([i for i in range(min_len)],x[i][:min_len],label=str(i))
mmymedian = np.median(clipx,axis=0)
mmymean = np.mean(clipx,axis=0)
plt.plot([i for i in range(min_len)],mmymedian,label="mmymedian")
# plt.plot([i for i in range(min_len)],mmymean,label="mmymean")



root = "/home/zhousihan/src/MARL-Algorithms"
x0 = np.load(root+"/result/qmix/"+name+"/win_rates_0.npy")
x1 = np.load(root+"/result/qmix/"+name+"/win_rates_1.npy")
x2 = np.load(root+"/result/qmix/"+name+"/win_rates_2.npy")
x3 = np.load(root+"/result/qmix/"+name+"/win_rates_3.npy")
x4 = np.load(root+"/result/qmix/"+name+"/win_rates_4.npy")
x5 = np.load(root+"/result/qmix/"+name+"/win_rates_5.npy")
x6 = np.load(root+"/result/qmix/"+name+"/win_rates_6.npy")
x7 = np.load(root+"/result/qmix/"+name+"/win_rates_7.npy")
x = [x0,x1,x3,x4,x5,x6,x7]
min_len = min([len(i) for i in x])
clipx = [i[:min_len] for i in x]
# for i in range(len(x)):
#     plt.plot([i for i in range(min_len)],x[i][:min_len],label=str(i))
median = np.median(clipx,axis=0)
mean = np.mean(clipx,axis=0)
plt.plot([i for i in range(min_len)],median,label="qmixmedian")
# plt.plot([i for i in range(min_len)],mean,label="qmixmean")

root = "/home/zhousihan/src/MARL-Algorithms"
x0 = np.load(root+"/result/maven/"+name+"/win_rates_0.npy")
x1 = np.load(root+"/result/maven/"+name+"/win_rates_1.npy")
x = [x0,x1]
min_len = min([len(i) for i in x])
clipx = [i[:min_len] for i in x]
# for i in range(len(x)):
#     plt.plot([i for i in range(min_len)],x[i][:min_len],label=str(i))
median = np.median(clipx,axis=0)
mean = np.mean(clipx,axis=0)
plt.plot([i for i in range(min_len)],median,label="mavenmedian")
# plt.plot([i for i in range(min_len)],mean,label="mavenmean")
plt.title(name)
plt.legend()
plt.savefig(name+".png")
plt.clf()
# plt.savefig(name+"_median.png")

name = "8m_vs_9m"
x0 = np.load("./result/qmix/"+name+"/win_rates_3.npy")
plt.plot([i for i in range(len(x0))],x0,label = "my")
x0 = np.load(root+"/result/qmix/"+name+"/win_rates_0.npy")
plt.plot([i for i in range(len(x0))],x0,label = "qmix")
plt.title(name)
plt.legend()
plt.savefig(name+".png")
plt.clf()

name = "2c_vs_64zg"
x0 = np.load("./result/qmix/"+name+"/win_rates_3.npy")
plt.plot([i for i in range(len(x0))],x0,label = "my")
x0 = np.load(root+"/result/qmix/"+name+"/win_rates_0.npy")
plt.plot([i for i in range(len(x0))],x0,label = "qmix")
x0 = np.load(root+"/result/maven/"+name+"/win_rates_0.npy")
plt.plot([i for i in range(len(x0))],x0,label = "maven")
plt.title(name)
plt.legend()
plt.savefig(name+".png")