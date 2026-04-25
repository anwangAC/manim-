from manim import *

class ManimStart(Scene):
    def construct(self):
        self.camera.background_color = GREY
        t1=MathTex(r"F_{0}=0,F_{1}=1,F_{n}=F_{n-1}+F_{n-2}(n\ge2)")
        self.play(Write(t1))
        self.wait(4)
        self.play(t1.animate.to_edge(UP))
        
        t2=MathTex(r"F_{n}=r^{n} ")
        self.play(Write(t2))
        self.wait(4)

        t3=MathTex(r"F_{n}=F_{n-1}+F_{n-2}")
        self.play(ReplacementTransform(t2,t3))
        self.wait(2)

        t4=MathTex(r"r^{n}=r^{n-1}+r^{n-2} ")
        self.play(ReplacementTransform(t3,t4))
        self.wait(2)
        self.play(t4.animate.next_to(t1,DOWN))

        t5=MathTex(r"r^{n}\cdot r^{-(n-2)}=(r^{n-1}+r^{n-2})\cdot r^{-(n-2)}")
        t5.next_to(t4,DOWN)
        self.play(Write(t5))
        self.wait(4)

        t6=MathTex(r"r^{2}=r+1")
        t6.next_to(t4,DOWN)
        self.play(ReplacementTransform(t5,t6))
        self.wait(4)

        t7=MathTex(r"r^{2}-r-1=0")
        t7.next_to(t4,DOWN)
        self.play(ReplacementTransform(t6,t7))
        self.wait(4)

        t8=MathTex(r"r=\frac{1\pm\sqrt{1+4}}{2}=\frac{1\pm\sqrt{5}}{2}")
        t8.next_to(t7,DOWN)
        self.play(Write(t8))
        self.wait(4)

        t9=MathTex(r"\varphi=\frac{1+\sqrt{5}}{2},\psi=\frac{1-\sqrt{5}}{2}")
        t9.next_to(t8,DOWN)
        self.play(Write(t9))
        self.wait(4)

        self.play(FadeOut(t4,t7,t8))
        self.play(t9.animate.next_to(t1,DOWN))

        t10=MathTex(r"F_{n}=A\varphi^{n}+B\psi^{n}")
        t10.next_to(t9,DOWN)
        self.play(Write(t10))
        self.wait(4)

        t11=MathTex(r"n=0:F_{0}=A\varphi^{0}+B\psi^{0}=A+B=0,B=-A")
        t11.next_to(t10,DOWN)
        self.play(Write(t11))
        self.wait(4)

        t12=MathTex(r"n=1:F_{1}=A\varphi^{1}+B\psi^{1}=A\varphi-A\psi=A(\varphi-\psi)=1")
        t12.next_to(t11,DOWN)
        self.play(Write(t12))
        self.wait(8)

        gold_border = SurroundingRectangle(
            t9,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))

        t13=MathTex(r"A(\varphi-\psi)=A(\frac{1+\sqrt{5}}{2}-\frac{1-\sqrt{5}}{2})=A\sqrt{5}=1,A=\frac{1}{\sqrt{5}}")
        t13.next_to(t12,DOWN)
        self.play(Write(t13))
        self.wait(6)

        t14=MathTex(r"B=-A=-\frac{1}{\sqrt{5} }")
        t14.next_to(t13,DOWN)
        self.play(Write(t14))
        self.wait(6)

        self.play(FadeOut(t10,t11,t12,t13,t14))

        t15=MathTex(r"F_{n}=\frac{1}{\sqrt{5}}\varphi^{n}-\frac{1}{\sqrt{5}}\psi^{n}=\frac{1}{\sqrt{5}}(\varphi^{n}-\psi^{n})")
        self.play(Write(t15))
        self.wait(6)

        t16=MathTex(r"F_{n}=\frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^{n}-(\frac{1-\sqrt{5}}{2})^{n})",color=YELLOW)
        self.play(ReplacementTransform(t15,t16))
        gold_border = SurroundingRectangle(
            t16,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.wait(15)