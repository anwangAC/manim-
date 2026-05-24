from manim import *
import numpy as np

class ManimStart(MovingCameraScene):
    def construct(self):
    
        #题目
        t1=Text("题目：").to_edge(LEFT + UP)
        self.play(Write(t1))
        t2=MathTex(
            r"\frac{1}{x+y}+\frac{1}{y+z}+\frac{1}{z+x}=\frac{7}{6}",
            font_size=40,
            tex_to_color_map={"x": RED, "y": GREEN, "z": BLUE}
        ).shift(UP*1.5)
        self.play(Write(t2))
        t3=MathTex(
            r"\frac{z}{x+y}+\frac{x}{y+z}+\frac{y}{z+x}=11",
            font_size=40,
            tex_to_color_map={"x": RED, "y": GREEN, "z": BLUE}
        ).next_to(t2,DOWN)
        self.play(Write(t3))
        t4_1=Text("问：",font_size=40)
        t4_2=MathTex(r"x+y+z=?",font_size=40,tex_to_color_map={"x": RED, "y": GREEN, "z": BLUE})
        t4=VGroup(t4_1,t4_2).arrange(RIGHT,buff=0.15).next_to(t3,DOWN)
        self.play(Write(t4))
        self.wait(2)

        #过度场景
        self.play(FadeOut(t1,t4))
        group=VGroup(t2,t3)
        self.play(group.animate.to_edge(UP))
        number1=MathTex(r"(1)",font_size=40).to_edge(UR)
        number2=MathTex(r"(2)",font_size=40).next_to(t3,RIGHT)
        number2.to_edge(RIGHT)
        self.play(Write(number1),Write(number2))

        #开始作答
        t5_1 = Text("令", font_size=40)
        t5_2 = MathTex(
            r"{a}=x+y,{b}=y+z,{c}=z+x",
            tex_to_color_map={
                "x": RED, "y": GREEN, "z": BLUE,
                "{a}": ORANGE, "{b}": PURPLE, "{c}": YELLOW
            },
            font_size=40
        )
        t5_3 = Text("因此", font_size=40)
        t5_4 = MathTex(r"(1),(2),", font_size=40)
        t5_5 = Text("分别等价于", font_size=40)
        t5_6 = MathTex(r"(3),(4)", font_size=40)
        t5 = VGroup(t5_1, t5_2, t5_3, t5_4, t5_5, t5_6).arrange(RIGHT, buff=0.15).next_to(t3, DOWN)
        t5.to_edge(LEFT)
        self.play(Write(t5))

        t6 = MathTex(
            r"\frac{1}{{a}}+\frac{1}{{b}}+\frac{1}{{c}}=\frac{7}{6}",
            tex_to_color_map={
                "x": RED, "y": GREEN, "z": BLUE,
                "{a}": ORANGE, "{b}": PURPLE, "{c}": YELLOW
            },
            font_size=40
        ).next_to(t3, DOWN)
        t6.shift(DOWN * 1)

        t7 = MathTex(
            r"\frac{z}{{a}}+\frac{x}{{b}}+\frac{y}{{c}}=11",
            tex_to_color_map={
                "x": RED, "y": GREEN, "z": BLUE,
                "{a}": ORANGE, "{b}": PURPLE, "{c}": YELLOW
            },
            font_size=40
        ).next_to(t6, DOWN)
        number3=MathTex(r"(3)",font_size=40).next_to(t6,RIGHT)
        number3.to_edge(RIGHT)
        number4=MathTex(r"(4)",font_size=40).next_to(t7,RIGHT)
        number4.to_edge(RIGHT)
        self.play(Write(t6))
        self.play(Write(t7))
        self.play(Write(number3),Write(number4))
        self.wait(2)
        t8 = MathTex(
            r"\frac{-{a}+{b}+{c}}{2{a}}+\frac{{a}-{b}+{c}}{2{b}}+\frac{{a}+{b}-{c}}{2{c}}=11",
            tex_to_color_map={
                "{a}": ORANGE,
                "{b}": PURPLE,
                "{c}": YELLOW
            },
            font_size=40
        ).next_to(t6, DOWN)
        self.play(ReplacementTransform(t7,t8))

        self.play(self.camera.frame.animate.shift(DOWN * 3), run_time=1.2)
        t9 = MathTex(
            r"(\frac{{b}}{{a}}+\frac{{c}}{{a}}-1) + (\frac{{a}}{{b}}+\frac{{c}}{{b}}-1) + (\frac{{a}}{{c}}+\frac{{b}}{{c}}-1)=22",
            tex_to_color_map={
                "{a}": ORANGE,
                "{b}": PURPLE,
                "{c}": YELLOW
            },
            font_size=40
        ).next_to(t8, DOWN)
        number5=MathTex(r"(5)",font_size=40).next_to(t9,RIGHT).to_edge(RIGHT)
        self.play(Write(t9),Write(number5))
        self.wait(2)
        t10 = MathTex(
            r"\frac{{a}}{{b}}+\frac{{a}}{{c}}+\frac{{b}}{{a}}+\frac{{b}}{{c}}+\frac{{c}}{{a}}+\frac{{c}}{{b}}=25",
            tex_to_color_map={
                "{a}": ORANGE,
                "{b}": PURPLE,
                "{c}": YELLOW
            },
            font_size=40
        ).next_to(t8, DOWN)
        self.play(ReplacementTransform(t9,t10))
        t11_1=Text("令",font_size=40)
        t11_2 = MathTex(
            r"p = \frac{1}{{a}}, q = \frac{1}{{b}}, {r} = \frac{1}{{c}}",
            tex_to_color_map={
                "{a}": ORANGE,
                "{b}": PURPLE,
                "{c}": YELLOW,
                "p": PINK,
                "q": GOLD,
                "{r}": TEAL
            },
            font_size=40
        )
        t11_3=Text("因此上式等价于下式",font_size=40)
        t11=VGroup(t11_1,t11_2,t11_3).arrange(RIGHT, buff=0.15).next_to(t10, DOWN).to_edge(LEFT)
        self.play(Write(t11))

        t12=MathTex(
            r"\frac{q+{r}}{p}+\frac{p+{r}}{q}+\frac{p+q}{{r}}=25",
            tex_to_color_map={
                "p": PINK,
                "q": GOLD,
                "{r}": TEAL
            },
            font_size=40
        ).next_to(t10, DOWN).shift(DOWN*1)
        number6=MathTex(r"(6)",font_size=40).next_to(t12,RIGHT).to_edge(RIGHT)
        self.play(Write(t12),Write(number6))
        self.wait(2)
        t13=MathTex(
            r"\because p+q+{r}=\frac{1}{{a}}+\frac{1}{{b}}+\frac{1}{{c}}=\frac{7}{6}",
            tex_to_color_map={
                "{a}": ORANGE,
                "{b}": PURPLE,
                "{c}": YELLOW,
                "p": PINK,
                "q": GOLD,
                "{r}": TEAL
            },
            font_size=40
        ).next_to(t12,DOWN).to_edge(LEFT)
        self.play(Write(t13))
        self.play(self.camera.frame.animate.shift(DOWN * 3), run_time=1.2)
        t14=MathTex(r"\therefore (6)\Rightarrow(7)",font_size=40).next_to(t13,DOWN).to_edge(LEFT)
        self.play(Write(t14))
        t15=MathTex(
            r"\frac{\frac{7}{6}-p}{p}+\frac{\frac{7}{6}-{q}}{q}+\frac{\frac{7}{6}-r}{{r}}=25",
            tex_to_color_map={
                "p": PINK,
                "q": GOLD,
                "{r}": TEAL
            },
            font_size=40
        ).next_to(t12,DOWN).shift(DOWN*2 )
        number7=MathTex(r"(7)",font_size=40).next_to(t15,RIGHT).to_edge(RIGHT)
        self.play(Write(t15),Write(number7))
        self.wait(1)
        t16=MathTex(
            r"\frac{7}{6} (\frac{1}{p}+\frac{1}{q}+\frac{1}{{r}})-3=25",
            tex_to_color_map={
                "p": PINK,
                "q": GOLD,
                "{r}": TEAL
            },
            font_size=40
        ).next_to(t12,DOWN).shift(DOWN*2 )
        self.play(ReplacementTransform(t15,t16))
        self.play(self.camera.frame.animate.shift(DOWN * 3), run_time=1.2)
        t17=MathTex(
            r"{a}+{b}+{c}=2(x+y+z)=24",
            tex_to_color_map={
                "x": RED, "y": GREEN, "z": BLUE,
                "{a}": ORANGE, "{b}": PURPLE, "{c}": YELLOW
            },
            font_size=40
        ).next_to(t16,DOWN)
        self.play(Write(t17))
        t18=MathTex(
            r"x+y+z=12",
            tex_to_color_map={
                "x": RED, "y": GREEN, "z": BLUE,
            },
            font_size=40
        ).next_to(t17,DOWN).shift(DOWN*1)
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