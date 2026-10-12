import numpy as np

from pygarment.garmentcode import utils as garment_utils
from pygarment.pattern import utils as pattern_utils


def test_cross_2d_is_signed_scalar_on_numpy_2():
    assert pattern_utils.cross_2d([1, 0], [0, 1]) == 1
    assert pattern_utils.cross_2d([0, 1], [1, 0]) == -1
    assert garment_utils.cross_2d(np.array([1.0, 0.0]), np.array([0.0, 2.0])) == 2
