from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

points = [575,
          607,
          3842,
          3876,
          7092,
          7124,
          9794,
          9839]

# x
# np.array([[p[0], 0] for p in points])
points_x = np.array([[p, 0] for p in points])

plt.figure(figsize=(6, 1))
plt.scatter(points_x[:, 0], points_x[:, 1])
plt.ylim(-0.1, 0.1)
plt.yticks(np.arange(-0.1, 0.1, 0.1))
ax = plt.gca()
ax.xaxis.tick_top()
# plt.savefig("27.svg", bbox_inches='tight', pad_inches=0)
plt.show()


def GetSC(k):
    clf = KMeans(k, n_init='auto')
    predict_x = clf.fit_predict(points_x)
    # print(predict_x)

    # plt.figure(figsize=(6,6))
    # plt.scatter(points_x[:,0], points_x[:,1], c=predict_x)
    # plt.show()

    SC = silhouette_score(points_x, predict_x)
    coef.append([k, SC])
    return SC


coef = []
k = 2
SC_0 = -1

while (True):
    SC = GetSC(k)
    if k < len(points)-1:
        SC_0 = SC
        k += 1
    else:
        print(coef)
        coef_array = np.array(coef)
        plt.figure(figsize=(6, 6))
        plt.scatter(coef_array[:, 0], coef_array[:, 1])
        plt.plot(coef_array[:, 0], coef_array[:, 1])
        # plt.savefig("59.svg", bbox_inches='tight', pad_inches=0)
        plt.show()
        break

SCs = [co[1] for co in coef]
best = coef[SCs.index(max(SCs))]
best_k = best[0]
clf = clf = KMeans(best_k, n_init='auto')
label_x = clf.fit_predict(points_x)
plt.figure(figsize=(6, 1))
plt.scatter(points_x[:, 0], points_x[:, 1], c=label_x)
plt.ylim(-0.1, 0.1)
plt.yticks(np.arange(-0.1, 0.1, 0.1))
ax = plt.gca()
ax.xaxis.tick_top()
# plt.savefig("68.svg", bbox_inches='tight', pad_inches=0)
plt.show()
print(label_x)


# # y
# points_y = np.array([[0, p[1]] for p in points])
# plt.figure(figsize=(1, 3))
# plt.scatter(points_y[:, 0], points_y[:, 1])
# plt.xlim(-0.1, 0.1)
# plt.xticks(np.arange(-0.1, 0.1, 0.1))
# ax = plt.gca()
# ax.invert_yaxis()
# ax.xaxis.tick_top()
# plt.savefig("73.svg", bbox_inches='tight', pad_inches=0)
# plt.show()


# def GetSC(k):
#     clf = KMeans(k, n_init='auto')
#     predict_y = clf.fit_predict(points_y)
#     # print(predict_y)

#     # plt.figure(figsize=(6,6))
#     # plt.scatter(points_y[:,0], points_y[:,1], c=predict_y)
#     # plt.show()

#     SC = silhouette_score(points_y, predict_y)
#     coef.append([k, SC])
#     # print(coef)
#     return SC


# coef = []
# k = 2
# SC_0 = -1

# while (True):
#     SC = GetSC(k)
#     if k < 10:
#         SC_0 = SC
#         k += 1
#     else:
#         print(coef)
#         coef_array = np.array(coef)
#         plt.figure(figsize=(6, 6))
#         plt.scatter(coef_array[:, 0], coef_array[:, 1])
#         plt.plot(coef_array[:, 0], coef_array[:, 1])
#         plt.savefig("105.svg", bbox_inches='tight', pad_inches=0)
#         plt.show()
#         break

# best = coef[-2]
# best_k = best[0]
# clf = KMeans(best_k, n_init='auto')
# label_y = clf.fit_predict(points_y)
# plt.figure(figsize=(1, 3))
# plt.scatter(points_y[:, 0], points_y[:, 1], c=label_y)
# plt.xlim(-0.1, 0.1)
# plt.xticks(np.arange(-0.1, 0.1, 0.1))
# ax = plt.gca()
# ax.invert_yaxis()
# ax.xaxis.tick_top()
# plt.savefig("118.svg", bbox_inches='tight', pad_inches=0)
# plt.show()
# print(label_y)
