from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, -42, 2)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angeleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angeleRadians), -20 * cos(angeleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)


app = MyApp()
app.run()
