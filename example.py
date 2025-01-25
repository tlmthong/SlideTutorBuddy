from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP

config.video_dir = "./videos"

class DemoScene(PresentationScene):

    def end_fragment_loop(self):
        self.end_fragment(fragment_type=COMPLETE_LOOP)
        self.end_fragment()

    def construct(self):
        self.nar("What exactly is DERIVATION?")
        self.nar("Well, derive means takes something out of something")
        self.nar("In maths, derivation means create slope function out of the original function")
        self.nar("So...every function has their baby slope function")
        self.nar("Lets look at a few examples")
        self.nar("First Function is")
        self.narMath("y = x^2")
        self.nar("On the left handside is the original function")
        self.nar("On the right handside is the slope function")
        self.nar("The point will run through the original function")
        self.nar("And the point on the right show the corresponding slope")
        func = lambda x: x**2
        derivative_func = lambda x: 2* x
        self.animate_slope(func, derivative_func, -2, 4, 2, "y = 2x")
        self.nar("Well, As you can see its a straight line")
        self.nar("We predict that")
        self.narMath(r"\frac{d}{dx} x^2 = 2x")
        self.nar("Lets look at another example")
        self.narMath("y = 2x^3")
        func = lambda x: 2*x**3
        derivative_func = lambda x: 6*x**2
        self.animate_slope(func, derivative_func, -2,-16, 24, "y = 6x^2")
        self.nar("So far we predict that")
        # Explain
        text1 = MathTex(r"\frac{d}{dx} x^2").center()
        text2 = MathTex("2x").center()
        self.add(text1)
        self.wait(1)
        self.play(Transform(text1,text2))
        self.clear()
        self.nar("And...")
        text1 = MathTex(r"\frac{d}{dx} 2x^3").center()
        text2 = MathTex("6x^2").center()
        self.add(text1)
        self.wait(1)
        self.play(Transform(text1,text2))
        self.clear()
        self.nar("We can informally observed that")
        self.narMath(r"\frac{d}{dx} a x^b = a b x^{b-1}")
        self.nar("Lets look at another example")
        self.narMath("y = x^4")
        func = lambda x: x**4
        derivative_func  = lambda x: 4*x**3
        self.animate_slope(func, derivative_func, -2,-16, -32, "y = 4x^3")
        self.nar("How about")
        self.narMath("y = 1/x")
        self.nar("This example I would leave for you to prove")
        self.nar("Try to use the property we observe")
        self.nar("Hint:")
        self.narMath(r"\frac{1}{x} = x^{-1}")
        self.nar("So far we only deal with single term, how about multiple terms")
        self.narMath("x^3 + x^2")
        self.nar("Lets take a microscope and explore this!")
        self.clear()
        self.explainProp()
        self.clear()
        self.nar("This means that you just need to derive each term individually")
        self.nar("And then add or subtract them like the original function")
        self.nar("And now you know")
        self.nar("How to do derivative")
    def explainProp(self):
        self.end_fragment()
        func = lambda x : x**2
        function_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-9, 9, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True}
        ).center()
        mainDot = Dot(function_axes.coords_to_point(1, func(1)))
        func_graph = function_axes.plot(func, color=BLUE)
        slope_line = function_axes.get_secant_slope_group(
            x=1, graph=function_axes.plot(func),
            dx=0.3, secant_line_color=YELLOW,
            secant_line_length=3
        )
        self.add(function_axes, mainDot, slope_line, func_graph)
        self.wait(2)
        slope = slope_line.copy().center().scale(3)
        self.play(FadeOut(mainDot), FadeOut(function_axes), FadeOut(func_graph), Transform(slope_line, slope, runtime = 1))
        self.wait()
        dx = Tex("dx").scale(0.5).center().shift(DOWN)
        dy = Tex("dy").scale(0.5).center().shift(RIGHT)
        self.add(dx, dy)
        self.wait()
        self.talk("dx is the change in x")
        self.talk("and dy is the change in y")
        self.talk("We assume that dx is really small")
        self.talk("but all dx in the universe is the same")
        self.talk("At the same x coordinate, lets takes the slope of the other function")
        self.clear()
        axe = Axes(
            x_range=[0,8,1],
            y_range=[0,8,1],
            x_length=6,
            y_length=6,
        ).center()
        
        firstLine = axe.plot(lambda x: 0.25*x, color=YELLOW)
        secondLine = axe.plot(lambda x: 3/8*x, color=BLUE)
        thirdLine = axe.plot(lambda x: 5/8*x, color=GREEN)
        eq1 = Text("Slope of x^2").next_to(firstLine).scale(0.5).shift(UP, LEFT)
        eq2 = Text("Slope of x^3").next_to(secondLine).scale(0.5).shift(UP, LEFT)
        eq3 = Text("Resulting Slope").next_to(thirdLine).scale(0.5).shift(UP*2, LEFT)
        self.add(axe, firstLine, secondLine, thirdLine, eq1,eq2,eq3)
        self.wait()
        self.talk("because we made an assumpution that all dx is the same")
        self.talk("then with the same starting point")
        self.talk("dy of the resulting slope")
        self.talk("is simply the sum of 2 other function")
        self.talk("so the slope of the resulting function"
        )
        self.talk("is simply add two of the slope up!!!!!")
        self.talk("BOOOM!! we got a new property!!!!")
        self.talk("(f(x)+g(x))' = f'(x) + g'(x)")
    def talk(self,string):
        text = Tex(string).scale(0.7)
        text.to_edge(DOWN)
        self.add(text)
        self.end_fragment()
        self.play(FadeOut(text))
    def nar(self, text):
        script = Tex(text)
        script.center()
        script.scale(0.8)
        self.play(FadeIn(script), run_time = 0.5)
        self.end_fragment()
        self.play(FadeOut(script), run_time = 0.5)
    def narMath(self, text):
        script = MathTex(text)
        script.scale(0.8)
        script.center()
        self.play(FadeIn(script), run_time = 0.5)
        self.end_fragment()
        self.play(FadeOut(script), run_time = 0.5)
    def animate_slope(self, mainFunc, dFunc, xCoor, yCoor, diff, equation):
        # Define the axes for the function and its derivative
        function_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-9, 9, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True}
        ).to_edge(LEFT, buff=1)
        
        derivative_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True}
        ).to_edge(RIGHT, buff=1)
        
        # func = lambda x: x**2
        func = mainFunc
        # derivative_func = lambda x: 2 * x
        derivative_func = dFunc

        # Plot the function and its derivative
        func_graph = function_axes.plot(func, color=BLUE)
        derivative_graph = derivative_axes.plot(derivative_func, color=GREEN)
        equa = MathTex(equation)
        equa.next_to(derivative_axes, ORIGIN).shift(UP, RIGHT)
        equa.scale(0.8)
        self.play(Create(function_axes), Create(derivative_axes), Create(func_graph))

        # Animate the slope and its derivative
        # self.animateSlope(function_axes, derivative_axes, func,-2, 4, -4)
        self.animateSlope(function_axes, derivative_axes, func,xCoor, yCoor, diff,equa, derivative_graph, derivative_func)
        self.wait(1)
        self.clear()
    

    def animateSlope(self,function_axes, dAxis, func, xC, yC, d, eq, dFunc, diffFunc):
        self.end_fragment()
        mainDot = Dot(function_axes.coords_to_point(-2, func(-2)))
        dDot = Dot(dAxis.coords_to_point(-2,diffFunc(-2)), color = BLUE)        
        trace = TracedPath(dDot.get_center, color = BLUE)  
        self.add(mainDot)
        self.add(dDot)
        self.add(trace)
        xC1 = xC
        yC1 = yC
        d1 = d
        slope_line = function_axes.get_secant_slope_group(
            x=-2, graph=function_axes.plot(func),
            dx=0.1, secant_line_color=YELLOW,
            secant_line_length=3
        )

        def update_slope_line(mob):
            mob.become(
                function_axes.get_secant_slope_group(
                    x=mainDot.get_center()[0] - function_axes.get_center()[0],
                    graph=function_axes.plot(func),
                    dx=0.1,
                    secant_line_color=YELLOW,
                    secant_line_length=3
                )
            )
        slope_line.add_updater(update_slope_line)
        self.add(slope_line)

        for i in range (1, 40):
            d1 = yC1
            xC1 += 0.1
            yC1 = func(xC1)
            d1 = yC1 - d1
            d1 = d1/0.1
            self.play(mainDot.animate.move_to(function_axes.coords_to_point(xC1, yC1)), run_time = 0.1, rate_func=linear)
            self.play(dDot.animate.move_to(dAxis.coords_to_point(xC1, d1)), run_time = 0.1, rate_func=linear)
        self.wait(2)
        self.play(FadeIn(dFunc), FadeIn(eq))
