from typing import Any, Dict
import torch as ch
import numpy as np
from threedb.controls.base_control import PostProcessControl

class CorruptionControl(PostProcessControl):
    """
    Applies some corruption
    """
    def __init__(self, root_folder: str):
        continuous_dims = {
            "a": (0, 1),
            "b": (0, 1),
            "noise": (0, 2)
        }
        super().__init__(root_folder,
                         continuous_dims=continuous_dims)

    def apply(self, render: ch.Tensor, control_args: Dict[str, Any]) -> ch.Tensor:
        no_err, msg = self.check_arguments(control_args)
        assert no_err, msg

        a, b, noise = (control_args['a'], control_args['b'],
                       control_args['noise'])
        img = render.numpy()
        img = img.transpose(1, 2, 0)
        noise_shape = img.shape[:2]
        img = (img * a + b)
        img = img + np.random.normal(0, noise, size=noise_shape)[:, :, None]
        img = np.clip(img, 0, 1)
        img = img.transpose(2, 0, 1)
        return ch.from_numpy(img).float()

Control = CorruptionControl
