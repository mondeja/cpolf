import pytest

from polf import line_xy


@pytest.mark.parametrize(
    'p0x,p0y,p1x,p1y,t,result',
    (
        (0, 0, 2, 0, .5, [1, 0]),
        (0, 0, 2, 0, 0, [0, 0]),
        (0, 0, 2, 0, 1, [2, 0]),

        (0, 0, .2, 0, .5, [.1, 0]),
        (0, 0, .2, 0, 0, [0, 0]),
        (0, 0, .2, 0, 1, [.2, 0]),

        (0, 0, 10, 10, .5, [5, 5]),
        (0, 0, 10, 10, .1, [1, 1]),
        (0, 0, 10, 10, .7, [7, 7]),

        (0, 0, -10, -10, .5, [-5, -5]),
        (0, 0, -10, -10, .1, [-1, -1]),
        (0, 0, -10, -10, .7, [-7, -7]),
    )
)
def test_line_xy(p0x, p0y, p1x, p1y, t, result):
    assert line_xy(p0x, p0y, p1x, p1y, t) == result
