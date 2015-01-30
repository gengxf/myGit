import matplotlib.pyplot as plt
import numpy as np
import jinrongBase

# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)
# x = np.linspace(0, 3, 100)
# for i in xrange(5):
#     plt.figure(1)
#     plt.plot(x, np.exp(i * x / 3))
#     plt.sca(ax1)
#     plt.plot(x, np.sin(i * x))
#     plt.sca(ax2)
#     plt.plot(x, np.cos(i * x))
# plt.show()

plt.figure(1)
sql_query = "select from_unixtime(apply_time, '%Y%m%d'),count(distinct mobile) from loan_fast_apply where apply_time > '1413475201' group by from_unixtime(apply_time, '%Y%m%d');"
data_dict, exmpt_dict = jinrongBase.select_query(sql_query)
x1 = []
y1 = []
count = jinrongBase.countItem(exmpt_dict) - 1
for i in range(count):
    x1.append(i)
for j in range(count):
    data = exmpt_dict[j]
    print j, data
    y1.append(data)
plot1 = plt.plot(x1, y1)
plt.show()
