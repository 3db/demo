"""
Defines the SunControl
"""

from threedb.try_bpy import bpy
import mathutils
import numpy as np
from typing import Any, Dict, Tuple
from threedb.controls.base_control import PreProcessControl


class SunControl(PreProcessControl):
    """Changes the elevation of the sun

    Note
    ----
    This control assumes that there is a Sky Texture node in the environment

    Continuous Dimensions:

    - ``elevation`` (float): The ratio of milk (range: [-pi, pi])
    """

    def __init__(self, root_folder: str):
        continuous_dims = {
            'elevation': (0, np.pi),
        }
        super().__init__(root_folder, continuous_dims=continuous_dims)


    def apply(self, context: Dict[str, Any], control_args: Dict[str, Any]) -> None:
        """Change the elevation of the sun

        Parameters
        ----------
        context : Dict[str, Any]
            The scene context
        control_args : Dict[str, Any]
            The arguments for this control, should have key ``elevation``
        """
        no_err, msg = self.check_arguments(control_args)
        assert no_err, msg

        elevation: float = control_args['elevation']
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_elevation = elevation

    def unapply(self, context: Dict[str, Any]) -> None:
        pass

Control = SunControl
