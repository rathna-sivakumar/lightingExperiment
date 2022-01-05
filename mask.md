# Masking Examples:

### fancy opengl code for projecting a mask onto an image
```python
import moderngl

class OpenGLMaskProjector:
    VERTEX_SHADER = """
        #version 330
        in vec3 in_vert;
        uniform mat3 projection;
        uniform mat3 rotation;
        uniform vec3 translation;
        uniform int width;
        uniform int height;
        void main() {
            vec3 homog = projection * ((rotation * in_vert) + translation);
            vec2 coord = vec2(homog.x / homog.z, homog.y / homog.z);
            vec2 ndc = vec2(coord.x / width * 2 - 1, coord.y / height * 2 - 1);
            gl_Position = vec4(ndc, 1.0, 1.0);
        }
    """
    FRAGMENT_SHADER = """
        #version 330
        out vec4 color;
        void main() {
            color = vec4(1.0f, 1.0f, 1.0f, 1.0f);
        }
    """

    def __init__(self, stl_path, size):
        self.size = size
        verts = np.fromfile(
            stl_path,
            dtype=np.dtype(
                [
                    ("norm", np.float32, [3]),
                    ("vec", np.float32, [3, 3]),
                    ("attr", np.uint16, [1]),
                ]
            ).newbyteorder("<"),
            offset=84,
        )["vec"].reshape(-1, 3)

        ctx = moderngl.create_context(standalone=True)

        self.prog = ctx.program(
            vertex_shader=self.VERTEX_SHADER,
            fragment_shader=self.FRAGMENT_SHADER,
        )

        self.prog["width"] = self.size
        self.prog["height"] = self.size

        vbo = ctx.buffer(verts.astype("f4").tobytes())
        self.vao = ctx.vertex_array(self.prog, vbo, "in_vert")
        self.fbo = ctx.simple_framebuffer((self.size, self.size))
        self.fbo.use()

    def make_mask(self, image, r_vec, t_vec, focal_length, centroid, bbox_size, imdims):
        origin = centroid - bbox_size / 2
        center = np.array(imdims) / 2 - origin
        focal_length *= self.size / bbox_size
        center *= self.size / bbox_size
        cam_matrix = np.array(
            [
                [focal_length, 0, center[1]],
                [0, focal_length, center[0]],
                [0, 0, 1],
            ],
            dtype=np.float32,
        )
        self.prog["projection"] = tuple(cam_matrix.T.flatten())

        self.prog["rotation"] = tuple(
            Rotation.from_rotvec(r_vec.squeeze()).as_matrix().T.flatten()
        )
        self.prog["translation"] = tuple(t_vec)
        self.fbo.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render(moderngl.TRIANGLES)
        binary_mask = np.frombuffer(self.fbo.read(), dtype=np.uint8).reshape(self.size, self.size, 3)[:, :, 0]
        return np.where((binary_mask == 0)[..., None], -1, image)
```

### instantiating previous class
```python
mask_gen = OpenGLMaskProjector(<path to stl file>, cropsize)
```
### creating binary mask
```python
mask = mask_gen.make_mask(cropped, r_vec, t_vec, focal_length, centroid, bbox_size, image.shape[:2])
```
explanation of variables:
* cropped: the image cropped to the bounding box specified in meta.json file
* r_vec: vector describing rotation of the spacecraft. Will need to convert from quaternion representation in the `pose` field of the meta.json file
* t_vec: vector describing the translation of the spacecraft. found in the `translation` field of the meta.json file
* focal_length: focal length of the camera in pixels. we will use the value 2988.57951638
* centroid: center point of bounding box in pixels (y,x)
* bbox_size: dimensions of bounding box in pixels (y,x)

### reading from json file
```python
import json
from scipy.spatial.transform import Rotation
import numpy as np


meta_path = <path to meta.json file>
with open(meta_path, "r") as f:
    meta = json.load(f)

pose = np.array(meta["pose"]) # reading in quaternion representation of pose
r_vec =  Rotation.from_quat(pose[[1, 2, 3, 0]]).as_rotvec() # converting to rotation vector
```