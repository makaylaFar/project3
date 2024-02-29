from panda3d.core import PandaNode, Loader, NodePath, Collision, CollisionSpehere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str)
        self.modelNode: NodePath = loader.loadModel(modelPath)

        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader.Model(" + modelPath +") did not return a proper PandaNode")