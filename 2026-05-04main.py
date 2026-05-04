from manim import *

class ManimStart(MovingCameraScene):
    def construct(self):
        
        #重要引理“留数定理”
        t1=Text(
            "重要引理：“留数法”",
            font_size=40,
            color=GREEN
        )
        self.play(Write(t1))
        self.wait(2)
        self.play(t1.animate.to_edge(UP + LEFT,buff=0.15))
        t2=Text(
            "留数法 是一种在部分分式分解中快速求系数的方法，\n"
            "它源于复变函数里的留数定理，\n"
            "但在这里只需要用到一个简单的代数结论，\n"
            "不需要你学过复变。",
            font_size=40,
            color=BLUE
        )
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)

        t3=MathTex(
            r"\frac{P(x)}{Q(x)}=\sum_{j=1}^{k}\frac{A_{j}}{x-a_{j}},Q(a_{k})=0",
            font_size=40,
        )
        self.play(Write(t3))
        self.wait(2)
        self.play(t3.animate.shift(UP * 3))
        t4=MathTex(
            r"\frac{P(x)(x-a_{k})}{Q(x)}=A_{k}+\sum_{j\ne k}^{}\frac{A_{j}(x-a_{k})}{x-a_{j}}",
            font_size=40
        ).next_to(t3 , DOWN,buff=0.15)
        self.play(Write(t4))
        self.wait(2)
        t5=MathTex(
            r"\lim_{x \to a_{k}} \frac{P(x)(x-a_{k})}{Q(x)}=\lim_{x \to a_{k}} A_{k}+\sum_{j\ne k}^{}\frac{A_{j}(x-a_{k})}{x-a_{j}}",
            font_size=40
        ).next_to(t4 , DOWN,buff=0.15)
        self.play(Write(t5))
        self.wait(2)
        t6=MathTex(
            r"\lim_{x \to a_{k}} \frac{[P(x)(x-a_{k})]^{'}}{Q^{'}(x)}=A_{k}",
            font_size=40
        ).next_to(t5 , DOWN,buff=0.15)
        self.play(Write(t6))
        self.wait(2)
        t7=MathTex(
            r"\frac{P(a_{k})}{Q^{'}(a_{k})}=A_{k}",
            font_size=40
        ).next_to(t6 , DOWN,buff=0.15)
        self.play(Write(t7))
        self.wait(2)
        gold_border = SurroundingRectangle(
            t7,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        #证明

        # 第一步：分母的因式分解
        t8=MathTex(
            r"x^n + 1 = 0",
            font_size=40
        )
        self.play(Write(t8))
        self.wait(2)
        self.play(t8.animate.to_edge(UP + LEFT,buff=0.5))
        self.wait(2)
        t9=MathTex(
            r"x = e^{i\frac{\pi(1+2m)}{n}},\quad m=0,1,\dots,n-1",
            font_size=40
        ).next_to(t8,RIGHT,buff=1.5)
        self.play(Write(t9))
        self.wait(2)
        t10_1=Text("令",font_size=40)
        t10_2=MathTex(r"(-\omega_{k})^{n}=-1",font_size=40)
        t10_3=Text("所以",font_size=40)
        t10_4=MathTex(r"-w_{k}",font_size=40)
        t10_5=Text("为原方程的n个根",font_size=40)
        t10=VGroup(t10_1,t10_2,t10_3,t10_4,t10_5).arrange(RIGHT, buff=0.15)
        t10.next_to(t8,DOWN,aligned_edge=LEFT)
        self.play(Write(t10))
        self.wait(2)
        t11=MathTex(
            r"\frac{1}{1+x^n} = \sum_{k=0}^{n-1} \frac{A_k}{x + \omega_k}",
            font_size=40,
            color=BLUE
        ).next_to(t10,DOWN,aligned_edge=LEFT)
        self.play(Write(t11))
        self.wait(2)
        t12=MathTex(
            r"A_k = \frac{1}{n \omega_k^{-1}} = \frac{\omega_k}{n}",
            font_size=40
        ).next_to(t11,RIGHT,buff=1.5)
        self.play(Write(t12))
        self.wait(2)
        t13_1=Text("把",font_size=40)
        t13_2=MathTex(r"\omega_k",font_size=40)
        t13_3=Text("的值带入蓝色求和中可得",font_size=40)
        t13=VGroup(t13_1,t13_2,t13_3,).arrange(RIGHT, buff=0.15).next_to(t11,DOWN,aligned_edge=LEFT)
        self.play(Write(t13))
        self.wait(2)
        t14=MathTex(r"\frac{1}{1+x^n} = \sum_{k=0}^{n-1} \frac{\omega_k}{n(x + \omega_k)}= \sum_{k=0}^{n-1} \frac{e^{\frac{2\pi}{n}i\left(k-\frac{n+1}{2}\right)}} {n\left(x + e^{\frac{2\pi}{n}i\left(k-\frac{n+1}{2}\right)}\right)}",font_size=40).next_to(t13,DOWN,aligned_edge=LEFT)
        self.play(Write(t14))
        self.wait(2)
        gold_border = SurroundingRectangle(
            t14,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)

        self.play(FadeOut(*self.mobjects))
        t15=MathTex(r"\frac{1}{1+x^n}=\sum_{k=0}^{n-1} \frac{e^{\frac{2\pi}{n}i\left(k-\frac{n+1}{2}\right)}} {n\left(x + e^{\frac{2\pi}{n}i\left(k-\frac{n+1}{2}\right)}\right)}",color=YELLOW)
        self.play(Write(t15))
        gold_border = SurroundingRectangle(
            t15,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))