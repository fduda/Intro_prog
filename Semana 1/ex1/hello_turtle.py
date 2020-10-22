############################################################
# FILE: hello.py
# WRITER: Felipe Duda Wainberg, felipew, 341299881
# EXERCISE: intro2cs ex1 2020-2021
# DESCRIPTION: A program that draws a sky with stars on the
# users screen.
############################################################

import turtle  # Imports the turtle library


def draw_star():  # This function draws a star
    # The next two lines of code draw a line of the star
    turtle.forward(20)
    turtle.right(144)
    # The star has 5 lines, so we repeat the block above 4 more times
    turtle.forward(20)
    turtle.right(144)
    turtle.forward(20)
    turtle.right(144)
    turtle.forward(20)
    turtle.right(144)
    turtle.forward(20)
    turtle.right(144)

    turtle.penup()  # This function lifts the pen and stops the drawing


def draw_star_cluster():  # This function draws a cluster of stars
    # The next 4 lines draw a star and moves the pen to the location of the next star
    turtle.pendown()
    draw_star()  # Draws a star
    turtle.penup()
    turtle.forward(30)
    turtle.left(120)
    # The cluster has 3 stars, so we repeat the block above 2 more times
    turtle.pendown()
    draw_star()
    turtle.penup()
    turtle.forward(30)
    turtle.left(120)
    turtle.pendown()
    draw_star()
    turtle.penup()
    turtle.forward(30)
    turtle.left(120)
    turtle.penup()  # Lifts the pen and stops the drawing


def draw_skies():  # This function draws a sky of clusters
    # The next 4 draws a cluster and moves the pen to the next location
    draw_star_cluster()  # Draws a cluster
    turtle.left(10)
    turtle.penup()
    turtle.forward(150)
    # The sky has 5 clusters, so we run the block above 4 more times
    draw_star_cluster()
    turtle.left(10)
    turtle.penup()
    turtle.forward(150)

    draw_star_cluster()
    turtle.left(270)
    turtle.penup()
    turtle.forward(150)

    draw_star_cluster()
    turtle.left(270)
    turtle.penup()
    turtle.forward(150)

    draw_star_cluster()  # Draws the last cluster


draw_skies()  # Executes the function above and draws a sky with clusters of stars
