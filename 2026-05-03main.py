from manim import *

class ManimStart(MovingCameraScene):
    def construct(self):
        #设置背景颜色为灰色
        self.camera.background_color = GREY
        
        #问题导入，展示所求积分
        t1=MathTex(r"\int\frac{1}{x^{4}+1}dx")
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)

        #对被积式因式分解
        t2=MathTex(r"\frac{1}{x^{4}+1}",font_size=40)
        self.play(Write(t2))
        self.wait(2)
        self.play(t2.animate.to_edge(UP + LEFT))
        self.wait(2)
        t3 = MathTex(
            r"=\frac{1}{ {{x^{4}+1+2x^{2}}} {{-2x^{2}}}}",
            font_size=40
        ).next_to(t2, RIGHT)
        self.play(Write(t3))
        self.wait(2)
        self.play(t3[1].animate.set_color(YELLOW))
        self.play(t3[1].animate.set_color(WHITE))
        t4=MathTex(
            r"=\frac{1}{ {{(x^{2}+1)^{2}-2x^{2}}} }",
            font_size=40
        ).next_to(t3, RIGHT)
        self.play(Write(t4))
        self.wait(2)
        self.play(t4[1].animate.set_color(YELLOW))
        self.play(t4[1].animate.set_color(WHITE))
        self.wait(2)
        t5=MathTex(r"=\frac{1}{(x^{2}+1+\sqrt{2}x)(x^{2}+1-\sqrt{2}x)}",font_size=40)
        t5.next_to(t2, DOWN, aligned_edge=LEFT)
        self.play(Write(t5))
        self.wait(2)
        t6=MathTex(r"=\frac{Ax+B}{x^{2}+1+\sqrt{2}x}+\frac{Cx+D}{x^{2}+1-\sqrt{2}x}",font_size=40).next_to(t5, RIGHT)
        self.play(Write(t6))
        self.wait(2)
        t7=MathTex(r"\because A=\frac{\sqrt{2}}{4},B=\frac{1}{2},C=-\frac{\sqrt{2}}{4},D=\frac{1}{2}",font_size=40)
        t7.next_to(t5, DOWN, aligned_edge=LEFT)
        self.play(Write(t7))
        self.wait(2)
        t8=MathTex(r"\therefore \frac{1}{x^{4}+1}=\frac{\frac{\sqrt{2}}{4}x+\frac{1}{2}}{x^{2}+1+\sqrt{2}x}+\frac{-\frac{\sqrt{2}}{4}x+\frac{1}{2}}{x^{2}+1-\sqrt{2}x}",font_size=40)
        t8.next_to(t7, DOWN, aligned_edge=LEFT)
        self.play(Write(t8))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(DOWN * 3), run_time=0.8)
        t9=MathTex(r"(x^{2}+1\pm\sqrt{2}x)^{'}=2x\pm\sqrt{2}",font_size=40,color=ORANGE).next_to(t8,RIGHT)
        self.play(Write(t9))
        gold_border = SurroundingRectangle(
            t9,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)
        t10=MathTex(r"\because \frac{\sqrt{2}}{4}x+\frac{1}{2}=\frac{\sqrt{2}}{8}(2x+\sqrt{2})+\frac{1}{4},\frac{\sqrt{2}}{4}x+\frac{1}{2}=-\frac{\sqrt{2}}{8}(2x-\sqrt{2})+\frac{1}{4}",font_size=40)
        t10.next_to(t8, DOWN, aligned_edge=LEFT)
        self.play(Write(t10))
        self.wait(2)
        t11=MathTex(r"\therefore \frac{1}{x^4+1} = \frac{\sqrt{2}}{8}\left( \frac{2x+\sqrt{2}}{x^2+\sqrt{2}x+1} \right) + \frac{1}{4}\left( \frac{1}{x^2+\sqrt{2}x+1} \right) - \frac{\sqrt{2}}{8}\left( \frac{2x-\sqrt{2}}{x^2-\sqrt{2}x+1} \right) + \frac{1}{4}\left( \frac{1}{x^2-\sqrt{2}x+1} \right)",font_size=40)
        t11.next_to(t10, DOWN, aligned_edge=LEFT)
        self.play(Write(t11))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(RIGHT * 6), run_time=1.2)
        self.wait(2)
        self.play(self.camera.frame.animate.shift(LEFT * 6), run_time=1.2)
        self.wait(2)
        self.play(self.camera.frame.animate.shift(DOWN * 3.3), run_time=1.2)
        self.wait(2)

        #逐项积分
        t12=MathTex(r"\int \frac{2x \pm \sqrt{2}}{x^2 \pm \sqrt{2}x + 1} \, dx = \ln|x^2 \pm \sqrt{2}x + 1| + C",font_size=40).next_to(t11,DOWN,aligned_edge=LEFT)
        self.play(Write(t12))
        self.wait(2)
        t13=MathTex(r"x^2 \pm \sqrt{2}x + 1 = \left(x \pm \frac{\sqrt{2}}{2}\right)^2 + \frac{1}{2}",font_size=40,color=ORANGE).next_to(t12,DOWN,aligned_edge=LEFT)
        self.play(Write(t13))
        gold_border = SurroundingRectangle(
            t13,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)
        t14=MathTex(r"\int \frac{1}{x^2 \pm \sqrt{2}x + 1} \, dx = \sqrt{2} \arctan\left(\sqrt{2}x \pm 1\right) + C",font_size=40).next_to(t13,DOWN,aligned_edge=LEFT)
        self.play(Write(t14))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(DOWN * 3.5), run_time=1.2)
        t15=MathTex(r"\int \frac{1}{1+x^4} \, dx = \frac{\sqrt{2}}{8} \ln\left| \frac{x^2+\sqrt{2}x+1}{x^2-\sqrt{2}x+1} \right| + \frac{\sqrt{2}}{4} \left[ \arctan(\sqrt{2}x+1) + \arctan(\sqrt{2}x-1) \right] + C",font_size=40).next_to(t14,DOWN,aligned_edge=LEFT)
        self.play(Write(t15))
        self.wait(2)
        self.play(self.camera.frame.animate.shift(RIGHT * 6), run_time=1.2)
        self.wait(2)
        self.play(self.camera.frame.animate.shift(LEFT * 6), run_time=1.2)
        self.wait(2)
        t16=MathTex(r"\arctan u + \arctan v = \arctan\left(\frac{u+v}{1-uv}\right)",font_size=40,color=ORANGE).next_to(t15,DOWN,aligned_edge=LEFT)
        self.play(Write(t16))
        gold_border = SurroundingRectangle(
            t16,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)
        t17=MathTex(r"\arctan(\sqrt{2}x+1) + \arctan(\sqrt{2}x-1) = \arctan\left( \frac{\sqrt{2}x}{1-x^2} \right)",font_size=40).next_to(t16,DOWN,aligned_edge=LEFT)
        self.play(Write(t17))
        self.wait(2)
        t18=MathTex(r"\int \frac{1}{1+x^4} \, dx = \frac{\sqrt{2}}{8} \ln\left| \frac{x^2+\sqrt{2}x+1}{x^2-\sqrt{2}x+1} \right| + \frac{\sqrt{2}}{4} \arctan\left( \frac{\sqrt{2}x}{1-x^2} \right) + C",font_size=40,color=YELLOW).next_to(t17,DOWN,aligned_edge=LEFT)
        self.play(Write(t18))
        gold_border = SurroundingRectangle(
            t18,
            color=GOLD,
            buff=0.15,         
            corner_radius=0.1,  
            stroke_width=6      
        )
        self.play(Create(gold_border))
        self.play(FadeOut(gold_border))
        self.wait(2)

        #展示全过程
        self.play(self.camera.frame.animate.shift(UP * 9.8), run_time=1.2)
        self.play(self.camera.frame.animate.shift(DOWN * 9.8), run_time=7)