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

    def draw(self):
        turtle.pd()
        vertices = self.get_vertices()
        angles = self.get__angles()
        edges = self.get__edges()
        for i in range(len(vertices[0])):
            turtle.fd(100*edges[i])
            turtle.left(180-angles[i])
        turtle.done()
    
    def perimeter(self):
        edges = self.get__edges()
        perimeter = sum(edges)
        return perimeter
    
    def is_convex(self):
        angles = self.get__angles()
        counter = 0
        for angle in angles:
            if angle <180:
                counter += 1
        if counter == len(angles):
            return True
        else:
            return False
        
    def translate(self, x, y):
        vertices = self.get_vertices()
        new_vertices_x = []
        new_vertices_y = []
        for vert in vertices[0]:
            new_vertices_x.append(vert+x)
        for vert in vertices[1]:
            new_vertices_y.append(vert+y)
        
        self.__x = new_vertices_x
        self.__y = new_vertices_y

    def list_of_points_cartesian(self):
        vertices = self.get_vertices()
        list_of_points = []
        for i in range(len(vertices[0])):
            list_of_points.append([vertices[0][i],vertices[1][i]])
        return list_of_points

    def list_of_points_polar(self):
        list_of_points_polar = []
        list_of_points_cartesian = self.list_of_points_cartesian()
        for point in list_of_points_cartesian:
            list_of_points_polar.append(self.convert_cartesian_to_polar(point))
        return list_of_points_polar

    def rotate(self, alpha):
        points_polar_in_degrees = self.list_of_points_polar()
        points_cartesian = []
        new_vertices_x = []
        new_vertices_y = []
        

        for point in points_polar_in_degrees:
            point[1] += alpha
        
        for point in points_polar_in_degrees:
            points_cartesian.append(self.convert_polar_to_cartesian(point))
        
        for point in points_cartesian:
            new_vertices_x.append(point[0])
            new_vertices_y.append(point[1])
            

        self.__x = new_vertices_x
        self.__y = new_vertices_y

    def distance_between_points(self, point_1, point_2):
        delta_x = point_1[0] - point_2[0]
        delta_y = point_1[1] - point_2[1]
        distance = math.sqrt(delta_x**2 + delta_y**2)
        return distance

    def polar_angle(self, point):
        x_coord = point[0]
        y_coord = point[1]

        if x_coord > 0 and y_coord > 0:
            theta = math.atan(y_coord/x_coord)
        elif x_coord < 0 and y_coord >0:
            theta = math.pi - math.atan(-(y_coord/x_coord))
        elif x_coord < 0 and y_coord < 0:
            theta = math.pi + math.atan(y_coord/x_coord)
        elif x_coord > 0 and y_coord < 0:
            theta = 2*math.pi - math.atan(-(y_coord/x_coord))
        
        if y_coord == 0 and x_coord > 0:
            theta = 0
        elif y_coord ==0 and x_coord < 0:
            theta = math.pi
        elif x_coord == 0 and y_coord > 0:
            theta = math.pi/2
        elif x_coord == 0 and y_coord < 0:
            theta = -(math.pi)/2 
        elif x_coord == 0 and y_coord == 0:
            theta = 0
        return math.degrees(theta)  # In degrees.

    def convert_cartesian_to_polar(self, point):
        radius = self.distance_between_points(point, (0,0))
        theta =  self.polar_angle(point)
        return [radius, theta]

    def convert_polar_to_cartesian(self, point):
        radius = point[0]
        theta = math.radians(point[1])  # In radians.
        x_coord = radius*math.cos(theta)
        y_coord = radius*math.sin(theta)
        return [x_coord, y_coord]




        
    





    



# print("SQUARE")
# square = Polygon([0,2,2,0],[0,0,2,2])
# print("VERTICES==>" ,square.get_vertices())
# print("ANGLES==>", square.get__angles())
# print("EDGES==>", square.get__edges())
# square.draw()
# print("===============================")

# print("Regular Pentagon")

# pentagon = Polygon([0, 1, 1.31, 0.5, -0.31],[0, 0, 0.95, 1.54, 0.95])
# print("VERTICES==>",pentagon.get_vertices())
# print("ANGLES==>", pentagon.get__angles())
# print("EDGES==>", pentagon.get__edges())
# pentagon.draw()

# print("===============================")
# print("Non regular hexagon")

nrhexagon = Polygon([0, 2, 3, 2, 1, -1], [0, 0, 1, 2, 2, 1])


print("=====Hexagono original=====")
print("VERTICES==>",nrhexagon.get_vertices())
print("ANGLES==>", nrhexagon.get__angles())
print("EDGES==>", nrhexagon.get__edges())
# nrhexagon.draw()




nrhexagon.rotate(90)

print("=====Hexagono rotacionado=====")

print("VERTICES==>",nrhexagon.get_vertices())
print("ANGLES==>", nrhexagon.get__angles())
print("EDGES==>", nrhexagon.get__edges())







# test_square = Polygon([1, -1, -1, 1], [1, 1, -1 ,-1])

# print(nrhexagon.list_of_points_cartesian())
# print(nrhexagon.list_of_points_polar())



# print(convert_polar_to_cartesian([3.1622776601683795, 18.43494882292201]))
