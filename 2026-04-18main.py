from manim import *

class ManimStart(Scene):
    def construct(self):
        self.camera.background_color = GREY
        t1=Text("考虑一个在单位圆上的复平面的点")
        self.play(Write(t1))
        self.play(t1.animate.to_edge(UP))
        t2=MathTex(r"A=e^{i\theta } =\cos \theta+i\sin \theta").next_to(t1,DOWN)
        self.play(Write(t2))
        self.wait(2)
        t3_1=Text("令")
        t3_2=MathTex(r"\theta=\alpha +\beta")
        t3_3=Text("，因此可得：")
        t3_group=VGroup(t3_1,t3_2,t3_3)
        t3_group.arrange(RIGHT)
        t3_group.next_to(t2,DOWN)
        self.play(Write(t3_group))
        self.wait(2)
        t4=MathTex(r"e^{i(\alpha +\beta)}=e^{i\alpha} \cdot e^{i\beta}=(\cos\alpha+i\sin \alpha)(\cos \beta+i\sin \beta)").next_to(t3_group,DOWN)
        self.play(Write(t4))
        self.wait(4)
        t5=MathTex(r"\cos \alpha\cos \beta+i\cos \alpha\sin \beta +i\sin \alpha\cos \beta +i^{2} \sin \alpha\sin \beta ").next_to(t3_group,DOWN)
        self.play(ReplacementTransform(t4,t5))
        self.wait(4)
        t6=MathTex(r"(\cos \alpha \cos \beta -\sin \alpha \sin \beta)+i(\sin \alpha \cos \beta +\cos \alpha \sin \beta)").next_to(t3_group,DOWN)
        self.play(ReplacementTransform(t5,t6))
        self.wait(4)
        t7=MathTex(r"\cos (\alpha +\beta )=\cos \alpha \cos \beta -\sin \alpha \sin \beta ").next_to(t6,DOWN)
        t8=MathTex(r"\sin (\alpha +\beta )=\sin \alpha \cos \beta +\sin \beta \cos \alpha ").next_to(t7,DOWN)
        self.play(Write(t7))
        self.play(Write(t8))
        self.wait(2)
        t7_1=MathTex(r"\cos (\alpha -\beta )=\cos \alpha \cos \beta +\sin \alpha \sin \beta ").next_to(t6,DOWN)
        self.play(ReplacementTransform(t7,t7_1))
        t8_1=MathTex(r"\sin (\alpha -\beta )=\sin \alpha \cos \beta -\sin \beta \cos \alpha ").next_to(t7_1,DOWN)
        self.play(ReplacementTransform(t8,t8_1))
        t7_2=MathTex(r"\cos (\alpha \pm \beta )=\cos \alpha \cos \beta \mp \sin \alpha \sin \beta ",color=YELLOW).next_to(t6,DOWN)
        self.play(ReplacementTransform(t7_1,t7_2))
        t8_2=MathTex(r"\sin (\alpha \pm \beta )=\sin \alpha \cos \beta \pm \sin \beta \cos \alpha ",color=YELLOW).next_to(t7_2,DOWN)
        self.play(ReplacementTransform(t8_1,t8_2))
        t7_t8_group=VGroup(t7_2,t8_2)
        gold_border = SurroundingRectangle(
            t7_t8_group,
            color=GOLD,
            buff=0.15,          # 边框与内容的间距
            corner_radius=0.1,  # 圆角
            stroke_width=6      # 边框粗细
        )
        self.play(Create(gold_border))
        self.wait(6)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)


        t9=MathTex(r"\sin 2\alpha =\sin (\alpha +\alpha )=\sin \alpha \cos \alpha +\sin \alpha \cos \alpha =2\sin \alpha \cos \alpha ").to_edge(UP)
        self.play(Write(t9))
        t10=MathTex(r"\cos 2\alpha =\cos (\alpha +\alpha )=\cos \alpha \cos \alpha -\sin \alpha \sin \alpha =\cos ^{2} \alpha -\sin ^{2} \alpha ").next_to(t9,DOWN)
        self.play(Write(t10))
        t9_1=MathTex(r"\sin 2\alpha =2\sin \alpha \cos \alpha ",color=YELLOW).next_to(t10,DOWN)
        self.play(ReplacementTransform(t9,t9_1))
        t10_1=MathTex(r"\cos 2\alpha  =\cos ^{2} \alpha -\sin ^{2} \alpha ",color=YELLOW).next_to(t9_1,DOWN)
        self.play(ReplacementTransform(t10,t10_1))
        t9_t10_group=VGroup(t9_1,t10_1)
        gold_border = SurroundingRectangle(
            t9_t10_group,
            color=GOLD,
            buff=0.15,          # 边框与内容的间距
            corner_radius=0.1,  # 圆角
            stroke_width=6      # 边框粗细
        )
        self.play(Create(gold_border))
        self.wait(6)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)

        t11=MathTex(r"\sin (\alpha +\beta )=\sin \alpha \cos \beta +\sin \beta \cos \alpha ,(1)",font_size=30).to_edge(UP)
        self.play(Write(t11))
        t11_1=MathTex(r"\sin (\alpha -\beta )=\sin \alpha \cos \beta -\sin \beta \cos \alpha ,(2)",font_size=30).next_to(t11,DOWN)
        self.play(Write(t11_1))
        t11_2=MathTex(r"\cos (\alpha +\beta )=\cos \alpha\cos \beta -\sin \alpha \sin \beta ,(3)",font_size=30).next_to(t11_1,DOWN)
        self.play(Write(t11_2))
        t11_3=MathTex(r"\cos (\alpha -\beta )=\cos \alpha\cos \beta +\sin \alpha \sin \beta ,(4)",font_size=30).next_to(t11_2,DOWN)
        self.play(Write(t11_3))
        self.wait(4)
        t11_4=MathTex(r"\begin{cases}x=\alpha +\beta  \\y=\alpha -\beta \end{cases}\Rightarrow \begin{cases}\alpha =\frac{x+y}{2} \\\beta =\frac{x-y}{2}\end{cases}",font_size=40).next_to(t11_3,DOWN)
        self.play(Write(t11_4))
        self.wait(4)
        t12=MathTex(r"(1)+(2)=\sin x+\sin y=2\sin \frac{x+y}{2} \cos \frac{x-y}{2} ",font_size=30).next_to(t11_4,DOWN)
        self.play(Write(t12))
        self.wait(4)
        t12_1=MathTex(r"(1)-(2)=\sin x-\sin y=2\cos \frac{x+y}{2}\sin \frac{x-y}{2} ",font_size=30).next_to(t12,DOWN)
        self.play(Write(t12_1))
        self.wait(4)

        t13=MathTex(r"(3)+(4)=\cos x+\cos y=2\cos \frac{x+y}{2} \cos \frac{x-y}{2} ",font_size=30).next_to(t12_1,DOWN)
        self.play(Write(t13))
        self.wait(4)
        t13_1=MathTex(r"(3)-(4)=\cos x-\cos y=-2\sin \frac{x+y}{2}\sin \frac{x-y}{2} ",font_size=30).next_to(t13,DOWN)
        self.play(Write(t13_1))
        self.wait(4)

        l1=MathTex(r"\sin x+\sin y=2\sin \frac{x+y}{2} \cos \frac{x-y}{2} ",font_size=30,color=YELLOW)
        l2=MathTex(r"\sin x-\sin y=2\cos \frac{x+y}{2}\sin \frac{x-y}{2} ",font_size=30,color=YELLOW)
        l3=MathTex(r"\cos x+\cos y=2\cos \frac{x+y}{2} \cos \frac{x-y}{2} ",font_size=30,color=YELLOW)
        l4=MathTex(r"\cos x-\cos y=-2\sin \frac{x+y}{2}\sin \frac{x-y}{2}  ",font_size=30,color=YELLOW)
        l_group=VGroup(l1,l2,l3,l4).arrange(DOWN)
        l_group.next_to(t11_4,DOWN)
        l1_group=VGroup(t12,t12_1,t13,t13_1)
        self.play(ReplacementTransform(l1_group,l_group))
        gold_border = SurroundingRectangle(
            l_group,
            color=GOLD,
            buff=0.15,          # 边框与内容的间距
            corner_radius=0.1,  # 圆角
            stroke_width=6      # 边框粗细
        )
        self.play(Create(gold_border))
        self.wait(6)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
