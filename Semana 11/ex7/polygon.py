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
        """"
        This method receives coordinates from a polygon and draws it using the Turtle class.
        """
        turtle.pd()
        vertices = self.get_vertices()
        angles = self.get__angles()
        edges = self.get__edges()
        for i in range(len(vertices[0])):
            turtle.fd(5*edges[i])  # The edges are multiplied by 5 so they wont be too small.
            turtle.left(180-angles[i])
        turtle.done()
    
    def perimeter(self):
        """
        This method receives coordinates from a polygon and returns its perimeter
        """
        edges = self.get__edges()
        perimeter = sum(edges)
        return perimeter
    
    def is_convex(self):
        """
        This method receives coordinates from a polygon. Returns True if the polygon is convex
        and false if it is not.
        """
        angles = self.get__angles()
        counter = 0
        for angle in angles:  # If any angle inside a polygon is greater than 180 deg, its not convex.
            if angle <180:
                counter += 1
        if counter == len(angles):
            return True
        else:
            return False
        
    def translate(self, x, y):
        """
        This method receives coordinates from a polygon and translates it.
        """
        vertices = self.get_vertices()
        new_vertices_x = []
        new_vertices_y = []
        for vert in vertices[0]:
            new_vertices_x.append(vert+x)  # Adds the translation in the x axis.
        for vert in vertices[1]:
            new_vertices_y.append(vert+y)  # Adds the translation in the y axis.
        
        # The next block change the orignal vertices.
        self.__x = new_vertices_x  
        self.__y = new_vertices_y

    def rotate(self, alpha):
        """
        This method receives coordinates from a polygon and rotates it.
        """
        points_polar_in_degrees = self.list_of_points_polar()  # Uses the points' polar form.
        points_cartesian = []
        new_vertices_x = []
        new_vertices_y = []
        

        for point in points_polar_in_degrees:  # Adds the rotation to the polar angle.
            point[1] += alpha
        
        for point in points_polar_in_degrees:  # Returns the points from polar to cartesian.
            points_cartesian.append(self.convert_polar_to_cartesian(point))
        
        for point in points_cartesian:
            new_vertices_x.append(point[0])
            new_vertices_y.append(point[1])
            

        # The next block change the orignal vertices.
        self.__x = new_vertices_x
        self.__y = new_vertices_y

    def __eq__(self, polygon2):
        """
        This method checks if two polygons are identical.
        """

        # The next block gets information about the first polygon.
        vertices_polygon1 = self.get_vertices()
        edges_polygon1 = self.get__edges()
        angles_polygon1 = self.get__angles()

        # The next block gets information about the second polygon.
        vertices_polygon2 = polygon2.get_vertices()
        edges_polygon2 = polygon2.get__edges()
        angles_polygon2 = polygon2.get__angles()


        if len(vertices_polygon1[0]) == len(vertices_polygon2[0]):
            for i in range(len(vertices_polygon1)):
                vertices_polygon1[i].sort()
                vertices_polygon2[i].sort()
        else:  # If the number of vertices is different, it's not the same polygon.
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
        """
        This method checks whether two polygons are congruent.
        """
        edges_polygon1 = self.get__edges()
        angles_polygon1 = self.get__angles()

        edges_polygon2 = polygon2.get__edges()
        angles_polygon2 = polygon2.get__angles()


        # Sorts the angles and edges list.
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
        """
        This method receives coordinates from a polygon and returns its area.
        """
        list_of_triangles = self.divide_into_triangles()
        list_of_areas = []
        triangles_in_list = []

        # Converts the list of coordinates into points.
        for triangle in list_of_triangles:
            triangle_in_list = self.convert_points_to_list(triangle)
            triangles_in_list.append(triangle_in_list)  # List of every triangle in the polygon.
        

        # The next block calculates the area of each triangle individualy
        for triangle in triangles_in_list:
            triangle_polygon = Polygon(triangle[0], triangle[1])
            middle_angle = triangle_polygon.get__angles()[0]

            edges_around_middle_angle = [triangle_polygon.get__edges()[0],\
                 triangle_polygon.get__edges()[1]]

            triangle_area = (edges_around_middle_angle[0]* \
                edges_around_middle_angle[1]*math.sin(math.radians(middle_angle)))/2

            list_of_areas.append(triangle_area)  # List of all the areas in the polygon.
        
        polygon_area = sum(list_of_areas)  # Sums all the areas to get the polygon area.

        return polygon_area

    def intersect(self, i, j):
        """
        This method receives coordinates from a polygon and checks whether two 
        edges of the polygon intersect into a vertex.
        """
        edges = self.get__edges()
        vertices_in_list = self.get_vertices()
        vertices_in_points = self.list_of_points_cartesian()  # Converts the vertices into points.


        if i == (len(edges)-1):
            line_eq_i = self.eq_line(vertices_in_points[0], vertices_in_points[i])
        else:
            line_eq_i = self.eq_line(vertices_in_points[i],vertices_in_points[i+1])
        
        if j == (len(edges)-1):
            line_eq_j = self.eq_line(vertices_in_points[0], vertices_in_points[j])
        else:
            line_eq_j = self.eq_line(vertices_in_points[j],vertices_in_points[j+1])

        intersection = self.lines_intersection(line_eq_i,line_eq_j)
        
        
        # The next block checks if the point of intersection is a vertex or not.
        if intersection in vertices_in_points:
            return True
        else:
            return False


    def is_valid(self):
        """
        This method receives coordinates from a polygon and checks whether it's valid.
        """
        vertices = self.get_vertices()

        if self.is_triangle():  # Every triangle is a valid polygon.
            return True
        elif len(vertices[0]) == 3 and self.is_triangle() == False:  # If the polygon has 3 edges but they coincide.
            return False


    def centroid(self):
        """
        This method receives coordinates from a polygon and returns its centroid.
        """
        vertices_in_list = self.get_vertices()
        vertices_in_points = self.list_of_points_cartesian()

        if len(vertices_in_list[0]) == 3:  # If the polygon is a triangle.
            centroid_x = sum(vertices_in_list[0])/len(vertices_in_list[0])
            centroid_y = sum(vertices_in_list[1])/len(vertices_in_list[1])
            return [centroid_x, centroid_y]
        



    def list_of_points_cartesian(self):
        """"
        This method receives coordinates from a polygon in the 
        form [x_0, x_1, ..., x_n],[y_0, y_1, ..., y_n] and returns 
        a list of coordinates in the form [x_0,y_0], [x_1, y_1]...[x_n, y_n].
        """

        vertices = self.get_vertices()
        list_of_points = []

        for i in range(len(vertices[0])):
            list_of_points.append([vertices[0][i],vertices[1][i]])
        return list_of_points

    def list_of_points_polar(self):
        """
        This method receives coordinates in carthesian form and 
        converts it to polar form.
        """
        list_of_points_polar = []
        list_of_points_cartesian = self.list_of_points_cartesian()

        for point in list_of_points_cartesian:
            list_of_points_polar.append(self.convert_cartesian_to_polar(point))
        return list_of_points_polar

    def convert_points_to_list(self, list_of_points):
        """
        This method receives coordinates from a polygon in the 
        form [x_0,y_0], [x_1, y_1]...[x_n, y_n]  and returns 
        a list of coordinates in the form [x_0, x_1, ..., x_n],[y_0, y_1, ..., y_n]
        """

        coordinates_x = []
        coordinates_y = []

        for point in list_of_points:
            coordinates_x.append(point[0])
            coordinates_y.append(point[1])

        return [coordinates_x, coordinates_y]

    def distance_between_points(self, point_1, point_2):
        """
        This method receives two points and calculate the
        distance between them.
        """
        delta_x = point_1[0] - point_2[0]
        delta_y = point_1[1] - point_2[1]
        distance = math.sqrt(delta_x**2 + delta_y**2)
        return distance

    def polar_angle(self, point):
        """
        This function receives a point and returns its polar angle.
        """
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
        """
        This method converts a point from cartesian form to polar form.
        """
        radius = self.distance_between_points(point, (0,0))
        theta =  self.polar_angle(point)
        return [radius, theta]

    def convert_polar_to_cartesian(self, point):
        """
        This method converts a point from polar form to cartesian form.
        """
        radius = point[0]
        theta = math.radians(point[1])  # In radians.
        x_coord = radius*math.cos(theta)
        y_coord = radius*math.sin(theta)
        return [x_coord, y_coord]

    def divide_into_triangles(self): 
        """
        This method divides a polygon into triangles.
        """
        list_of_vertices = self.get_vertices()
        list_of_points = self.list_of_points_cartesian()
        list_of_triangles = []

        for i, j in zip(list_of_points[1:], list_of_points[2:]):
            list_of_triangles.append([list_of_points[0], i,j])
        
        return list_of_triangles

    def is_triangle(self):
        """"
        This method checks if the polygon is a triangle.
        """
        list_of_points = self.list_of_points_cartesian()
        line = self.eq_line(list_of_points[0], list_of_points[1])

        if self.is_point_in_line(list_of_points[2], line):
            return False

        return True

    def eq_line(self, point1, point2):
        """
        This method receives two points and returns the line that connects them.
        """
        delta_y = point1[1] - point2[1]
        delta_x = point1[0] - point2[0]
        
        
        if delta_x != 0:
            inclination = delta_y/delta_x
            line = [1, inclination, -inclination*point1[0] + point1[1]]
        else:
            line = [0, -1, point1[0]]          
        return line
            
    def lines_intersection(self, line1, line2):
        """
        This method receives two lines and returns their intersection.
        """
        line1_ = [number*line2[1] for number in line1]
        line2_ = [number*line1[1] for number in line2]
        
        if line1[1] == line2[1]:
            return False

        equation = [line1_[0] - line2_[0], line1_[1] - line2_[1],\
                    line1_[2] - line2_[2]]

        intersection_y = equation[2] / equation[0]
        if line1[1] != 0:
            intersection_x = (intersection_y - line1[2])/line1[1]
        elif line1[0] == 0:
            intersection_x = line1[2]
        elif line2[0] == 0:
            intersection_x = line2[2]
        else:
            intersection_x = line2[2]/(-line2[1])

        return [round(intersection_x,5), round(intersection_y, 5)]

    def is_point_in_line(self, point, line):
        """
        This method receives a point and a line and checks if the point is in the line.
        """
        equation = [point[1]*line[0], point[0]*line[1], line[2]]
        
        if equation[0] == equation[1] + equation[2]:
            return True
        else:
            return False
