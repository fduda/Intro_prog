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
            turtle.fd(5*edges[i])
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

    def __eq__(self, polygon2):
        vertices_polygon1 = self.get_vertices()
        edges_polygon1 = self.get__edges()
        angles_polygon1 = self.get__angles()

        vertices_polygon2 = polygon2.get_vertices()
        edges_polygon2 = polygon2.get__edges()
        angles_polygon2 = polygon2.get__angles()

        if len(vertices_polygon1[0]) == len(vertices_polygon2[0]):
            for i in range(len(vertices_polygon1)):
                vertices_polygon1[i].sort()
                vertices_polygon2[i].sort()
        else:
            return False

        edges_polygon1.sort()
        edges_polygon2.sort()

        angles_polygon1.sort()
        angles_polygon2.sort()

        if angles_polygon1 == angles_polygon2 and \
             edges_polygon1 == edges_polygon2 and \
                 vertices_polygon1 == vertices_polygon2:
                 return True
        else:
            return False

    def is_congruent(self, polygon2):

        edges_polygon1 = self.get__edges()
        angles_polygon1 = self.get__angles()

        edges_polygon2 = polygon2.get__edges()
        angles_polygon2 = polygon2.get__angles()

        if len(angles_polygon1) == len(angles_polygon2):
            angles_polygon1.sort()
            angles_polygon2.sort()
            edges_polygon1.sort()
            edges_polygon2.sort()
        else:
            return False


        rounded_angles_poly1 = [round(angle, 11) for angle in angles_polygon1]
        rounded_angles_poly2 = [round(angle, 11) for angle in angles_polygon2]
        rounded_edges_poly1 = [round(edge, 11) for edge in edges_polygon1]
        rounded_edges_poly2 = [round(edge, 11) for edge in edges_polygon1]
        

        if rounded_angles_poly1 == rounded_angles_poly2 and \
             rounded_edges_poly1 == rounded_edges_poly2:
                 return True
        else:
            return False

    def area(self):
        list_of_triangles = self.divide_into_triangles()
        list_of_areas = []
        triangles_in_list = []

        for triangle in list_of_triangles:
            triangle_in_list = self.convert_points_to_list(triangle)
            triangles_in_list.append(triangle_in_list)
        
        for triangle in triangles_in_list:
            triangle_polygon = Polygon(triangle[0], triangle[1])
            middle_angle = triangle_polygon.get__angles()[0]
            edges_around_middle_angle = [triangle_polygon.get__edges()[0], triangle_polygon.get__edges()[1]]
            triangle_area = (edges_around_middle_angle[0]*edges_around_middle_angle[1]*math.sin(math.radians(middle_angle)))/2
            list_of_areas.append(triangle_area)
        
        polygon_area = sum(list_of_areas)

        return polygon_area


#########################################################################################


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

    def convert_points_to_list(self, list_of_points):

        coordinates_x = []
        coordinates_y = []

        for point in list_of_points:
            coordinates_x.append(point[0])
            coordinates_y.append(point[1])

        return [coordinates_x, coordinates_y]

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

    def divide_into_triangles(self): 
        list_of_vertices = self.get_vertices()
        list_of_points = self.list_of_points_cartesian()
        list_of_triangles = []

        for i, j in zip(list_of_points[1:], list_of_points[2:]):
            list_of_triangles.append([list_of_points[0], i,j])
        
        return list_of_triangles
        


        

    


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
# nrhexagon2 = Polygon([0, 2, 3, 2, 1, -1], [0, 0, 1, 2, 2, 1])


# print("=====Hexagono original=====")
# print("VERTICES==>",nrhexagon.get_vertices())
# print("ANGLES==>", nrhexagon.get__angles())
# print("EDGES==>", nrhexagon.get__edges())


# nrhexagon2.rotate(45)

# print("=====Hexagono rotacionado=====")

# print("VERTICES==>",nrhexagon2.get_vertices())
# print("ANGLES==>", nrhexagon2.get__angles())
# print("EDGES==>", nrhexagon2.get__edges())

# print("========HEXAGONO REGULAR========")
# hexagono = Polygon([0, 20, 30, 20, 0, -10], [0, 0, 17.32, 34.64, 34.64, 17.32])

# triangle1 = Polygon([0, 20, 30],[0, 0, 17.32])
# triangle1.draw()

# square = Polygon([0,2,2,0],[0,0,2,2])

# pentagon = Polygon([0, 3, 3.93, 1.5, -0.93], [0, 0, 2.85, 4.62, 2.85])
# triangle = Polygon([0, 3, 3.93], [0, 0, 2.85])

# print(triangle.get__angles())
# print(triangle.get__edges())


# print(pentagon.divide_into_triangles())
# print(pentagon.area())

weird_polygon = Polygon([-10.4, 30.4, 60.2, 40.01], [-10.4, 30.5, 10.2, 20.3])

print(nrhexagon.is_convex())