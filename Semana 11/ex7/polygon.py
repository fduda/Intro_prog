import turtle
import math


class Polygon:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__angles = [None]*len(x)
        self.__edges = [None]*len(x)

        self.compute__edges()
        self.compute__angles()

    def compute__angles(self):
        n = len(self.__x)
        for i in range(n):
            normalized_dot_prod = ((self.__x[i]-self.__x[i-1])*(self.__x[i]-self.__x[(i+1) % n]) +
                                   (self.__y[i]-self.__y[i-1])*(self.__y[i]-self.__y[(i+1) % n])) / \
                                  (self.__edges[i]*self.__edges[(i+1) % n])
            self.__angles[i] = math.acos(normalized_dot_prod) * 180 / math.pi  # radians to degrees
            A = [self.__y[i]-self.__y[i-1], self.__x[i-1]-self.__x[i],
                 self.__y[i]*(self.__x[i]-self.__x[i-1])-self.__x[i]*(self.__y[i]-self.__y[i-1])]  # equation for line

            if self.__x[(i+1) % n] * A[0] + self.__y[(i+1) % n] * A[1] + A[2] < 0:
                self.__angles[i] = 360 - self.__angles[i]

        if sum(self.__angles) > 180 * len(self.__x):
            for i in range(len(self.__x)):  # take other direction
                self.__angles[i] = 360 - self.__angles[i]

    def compute__edges(self):
        for i in range(len(self.__x)):
            self.__edges[i] = math.sqrt((self.__x[i] - self.__x[i - 1]) ** 2 + (self.__y[i] - self.__y[i - 1]) ** 2)

    def get__edges(self):
        return self.__edges

    def get__angles(self):
        return self.__angles

    def get_vertices(self):
        return [self.__x, self.__y]

