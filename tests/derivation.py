from manimlib import *

class formula(Scene):
    def construct(self):

        f1 = Tex(r"\hat{H} \psi_{n} = E_{n} \psi_{n}")
        f2 = Tex(r"\psi^{*}_{n} \hat{H} \psi_{n} = E_{n} \psi^{*}_{n} \psi_{n}")
        f3 = Tex(r"\int \psi^{*}_{n} \hat{H} \psi_{n} d \tau = E_{n} \int \psi^{*}_{n} \psi_{n} d \tau")
        f4 = Tex(r"\int \psi^{*}_{n} \psi_{n} d \tau = 1")
        f5 = Tex(r"\int \psi^{*}_{n} \hat{H} \psi_{n} d \tau = E_{n}")
        f6 = Tex(r"\frac{\partial}{\partial \lambda} \int \psi^{*}_{n} \hat{H} \psi_{n} d \tau = \frac{\partial E_{n} }{\partial \lambda}")
        f7 = Tex(r"\int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \hat{H} \psi_{n} d \tau + \int \psi^{*}_{n}  \frac{\partial(\hat{H} \psi_{n}) }{\partial \lambda} d \tau = \frac{\partial E_{n} }{\partial \lambda}")
        f8 = Tex(r"\frac{\partial(\hat{H} \psi_{n}) }{\partial \lambda} = \frac{\partial\hat{H} }{\partial \lambda} \psi_n + \hat{H}\frac{\partial \psi_{n} }{\partial \lambda}")
        f9 = Tex(r"\int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \hat{H} \psi_{n} d \tau + \int \psi^{*}_{n} \frac{\partial\hat{H} }{\partial \lambda} \psi_n d \tau + \int \psi^{*}_{n} \hat{H}\frac{\partial \psi_{n} }{\partial \lambda} d \tau = \frac{\partial E_{n} }{\partial \lambda}")
        f10 = Tex(r"\int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \hat{H} \psi_{n} d \tau =  E_{n} \int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \psi_{n} d \tau")
        f11 = Tex(r"\int \psi^{*}_{n} \hat{H}\frac{\partial \psi_{n} }{\partial \lambda} d \tau = \int \frac{\partial \psi_{n} }{\partial \lambda} (\hat{H} \psi_{n})^{*} d \tau = E_{n} \int \frac{\partial \psi_{n} }{\partial \lambda} \psi_{n}^{*} d \tau")
        f12 = Tex(r" E_{n} \int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \psi_{n} d \tau + \int \psi^{*}_{n} \frac{\partial\hat{H} }{\partial \lambda} \psi_n d \tau + E_{n}\int \frac{\partial \psi_{n} }{\partial \lambda} \psi^{*}_{n}  d \tau = \frac{\partial E_{n} }{\partial \lambda}")
        f13 = Tex(r" E_{n} (\int \frac{\partial \psi^{*}_{n} }{\partial \lambda} \psi_{n} d \tau + \int \frac{\partial \psi_{n} }{\partial \lambda} \psi^{*}_{n}  d \tau) = E_{n} (\frac{\partial}{\partial \lambda} \int \psi^{*}_{n} \psi_{n} d \tau) = E_{n} \frac{\partial 1 }{\partial \lambda} = 0")
        f14 = Tex(r"\int \psi^{*}_{n} \frac{\partial\hat{H} }{\partial \lambda} \psi_n d \tau = \frac{\partial E_{n} }{\partial \lambda}")

        self.play(Write(f1))

        self.wait()

        self.play(TransformMatchingShapes(f1, f2, path_arc = PI/2))

        self.wait()

        self.play(TransformMatchingShapes(f2, f3, path_arc = 0)) 

        self.wait()

        self.play(f3.to_edge, UP)

        self.wait()
        
        self.play(Write(f4))

        self.wait()

        self.clear()

        self.add(f3)

        self.play(f3.shift, DOWN*3)

        self.play(ReplacementTransform(f3, f5))

        self.wait()

        self.play(TransformMatchingShapes(f5, f6, path_arc = 0))

        self.wait()

        self.play(TransformMatchingShapes(f6, f7, path_arc = 0))

        self.wait()

        self.play(f7.to_edge, UP)

        self.wait()

        self.play(Write(f8))

        self.wait()

        self.remove(f8)

        self.play(f7.shift, DOWN*3)

        self.play(TransformMatchingShapes(f7, f9, path_arc = 0))

        self.wait()

        self.play(f9.to_edge, UP)

        self.wait()

        self.play(Write(f10))

        self.wait(2)

        self.remove(f10)

        self.play(Write(f11))

        self.wait(2)

        self.remove(f11)

        self.play(f9.shift, DOWN*3)

        self.play(TransformMatchingShapes(f9, f12, path_arc = 0))

        self.wait()

        self.play(f12.to_edge, UP)

        self.wait()

        self.play(Write(f13))

        self.wait(3)

        self.remove(f13)

        self.wait()

        self.play(f12.shift, DOWN*3)

        self.play(ReplacementTransform(f12, f14))

        self.wait(2)

        self.clear()

        cf = Text ("Made by ChemicalFiend.")

        lik = Text("Like. Share. Subscribe.")

        lik.scale(0.8)

        lik.set_color(PURPLE)

        cf.set_color(RED)

        self.play(Write(cf))

        self.play(cf.to_edge, UP)
        
        self.play(Write(lik))
        
        
        
        
        
        
        
        
