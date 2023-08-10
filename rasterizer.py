from gl import Renderer
import shaders


width = 500
height = 500

rend = Renderer(width, height)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

scaleDim = 400

#Medium shot
rend.glLoadModel(filename = "table.obj",
                texName = "tabletex.bmp",
                translate=(0, 0, -500),
                rotate=(0.3, 0, 0),
                scale=(scaleDim, scaleDim, scaleDim))

rend.glLookAt(camPos=(0, 50, 0),
                eyePos=(0, 0, -500))

rend.glRender()

rend.glFinish("mediumshot.bmp")

rend.glClearColor(0, 0, 0)
rend.glClear()
rend.objects = []

#Low angle
rend.glLoadModel(filename = "table.obj",
                texName = "tabletex.bmp",
                translate=(0, 0, -500),
                rotate=(0.3, 0, 0),
                scale=(scaleDim, scaleDim, scaleDim))

rend.glLookAt(camPos=(0, -100, 0),
                eyePos=(0, 150, -100))

rend.glRender()

rend.glFinish("lowangle.bmp")

rend.glClearColor(0, 0, 0)
rend.glClear()
rend.objects = []

#High angle
rend.glLoadModel(filename = "table.obj",
                texName = "tabletex.bmp",
                translate=(0, 0, -500),
                rotate=(0.3, 0, 0),
                scale=(scaleDim, scaleDim, scaleDim))

rend.glLookAt(camPos=(0, 200, 0),
                eyePos=(0, -220, -100))

rend.glRender()

rend.glFinish("highangle.bmp")

rend.glClearColor(0, 0, 0)
rend.glClear()
rend.objects = []

#Dutch angle
rend.glLoadModel(filename = "table.obj",
                texName = "tabletex.bmp",
                translate=(0, 0, -500),
                rotate=(0.3, 0, 0.1),
                scale=(scaleDim, scaleDim, scaleDim))

rend.glLookAt(camPos=(0, 50, 0),
                eyePos=(-20, 0, -500))

rend.glRender()

rend.glFinish("dutchangle.bmp")
