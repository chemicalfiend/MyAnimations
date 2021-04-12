from manimlib import *

class Formula(Scene):
    def construct(self):
        formula_tex1 = Tex(r"\begin{bmatrix}    cos(2 \pi / 3)  &  -sin(2 \pi / 3) & 0      \\    sin(2 \pi / 3)  &  cos(2 \pi /3) & 0 \\ 0 & 0 & 1      \end{bmatrix}  \begin{bmatrix}    x      \\  y \\ z      \end{bmatrix}")
        formula_tex1.scale(1)

        formula_tex2 = Tex(r"\left[\begin{array}{cc|c} cos(2 \pi / 3)  &  -sin(2 \pi / 3) & 0      \\    sin(2 \pi / 3)  &  cos(2 \pi /3) & 0 \\ \hline 0 & 0 & 1       \end{array}\right] \quad \left[\begin{array}{c} x \\ y \\ \hline z \end{array} \right]")
        
        formula_tex3 = Tex(r"\begin{bmatrix}    cos(2 \pi / 3)  &  -sin(2 \pi / 3)      \\    sin(2 \pi / 3)  &  cos(2 \pi /3) \\ \end{bmatrix}  \begin{bmatrix}    x      \\  y \\ \end{bmatrix}")
        formula_tex4 = Tex(r"\begin{bmatrix} 1 \end{bmatrix} \begin{bmatrix} z \end{bmatrix}")
        formula_tex3.scale(1)
        formula_tex2.scale(1)
        self.play(Write(formula_tex1))
        self.wait()
        self.play(Transform(formula_tex1, formula_tex2))
        self.wait()
        self.clear()
        self.play(Write(formula_tex3))
        self.wait()
        self.clear()
        self.play(Write(formula_tex4))
        self.wait()


