from turtle import*
def arbre(n, longueur):
    if n==0:
        color("red")
        forward(longueur)
        backward(longueur)
        color("black")
    else:
        long = longueur/3
        forward(long)
        left(40)
        arbre(n-1, 2*long)
        right(80)
        arbre(n-1, 2*long)
        left(40)
        backward(long)
left(90)
arbre(2, 250)
showturtle()
exitonclick()
