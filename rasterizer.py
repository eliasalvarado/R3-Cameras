from gl import Renderer
import shaders


width = 500
height = 500

rend = Renderer(width, height)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

scaleDim = 10

rend.glLoadModel(filename = "model.obj",
                texName = "model.bmp",
                translate=(width/2, height/2, 10),
                rotate=(0, 0, 0),
                scale=(scaleDim, scaleDim, scaleDim))


rend.glRender()

rend.glFinish("output.bmp")
