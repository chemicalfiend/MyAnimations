from manimlib import *

class rots (Scene):

    def construct (self):
        h = Text("The Rotations of a Square Form a Group")

        h.scale(0.75)

        h2 = Text("The Group Operation is a Composition of Rotations")

        h2.set_color(RED)

        h2.scale(0.65)

        c = Text("1) C4 - rotation by 90 degree")

        c.scale(0.75)

        c.shift(UP*2)

        c2 = Text("2) C4' - rotation by 180 degree")

        c2.scale(0.75)

        c2.shift(UP*2)

        c3 = Text("3) C4'' - rotation by 270 degree")

        c3.scale(0.75)

        c3.shift(UP*2)

        h.set_color(RED)

        c4 = Text("Composing C4'' and C4' we get a rotation by 450 degrees")

        c4.scale(0.5)

        c5 = Text("Which is the same as C4")

        c5.scale(0.75)

        s = Square() 

        P = Text("A")

        Q = Text("B")

        R = Text("C")

        S = Text("D")

        P.shift(UP + LEFT)

        Q.shift(UP + RIGHT)

        R.shift(DOWN + RIGHT)

        S.shift(DOWN + LEFT)

        sq = VGroup(s, P, Q, R, S)

        sq.save_state()

        self.play(Write(h))

        self.clear()

        self.play(h.to_edge, UP)
        
        self.play(Write(c))

        self.play(Rotate(sq, PI/2))

        self.wait()

        self.clear()

        sq.rotate(-PI/2)

        self.play(Write(c2))

        self.wait()

        self.play(Rotate(sq, PI))

        self.wait()

        self.clear()

        sq.rotate(-PI)

        self.play(Write(c3))

        self.wait()

        self.play(Rotate(sq, 3*PI/2))
        
        self.wait(2)

        self.clear()

        sq.rotate(-3*PI/2)

        self.play(Write(h2))

        self.play(h2.to_edge, UP)

        self.play(Write(c4))

        self.play(c4.shift, UP*2)

        self.play(Rotate(sq, PI))

        self.wait()

        self.play(Rotate(sq, 3*PI/2))

        self.wait(2)

        self.clear()

        c5.shift(UP*2)

        self.play(Write(c5))

        sq.rotate(-5 * PI/2)

        self.play(Rotate(sq, PI/2))

        self.wait()

        self.clear()

        cf = Text ("Made by ChemicalFiend.")

        lik = Text("Like. Share. Subscribe.")

        lik.scale(0.8)

        lik.set_color(PURPLE)

        cf.set_color(RED)

        self.play(Write(cf))

        self.play(cf.to_edge, UP)
        
        self.play(Write(lik))


