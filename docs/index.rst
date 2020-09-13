polf's documentation
====================

Simple library written with the Python C API to calculate points on lines.
It does not perform any checks on the passed data, but rather follows the
GIGO processing pattern.

I have written it with the main purpose of learning, but it may be useful in
some situation or it can serve as a reference to get you started in the
Python C API.

.. code-block:: bash

   pip install polf


Public API
~~~~~~~~~~

.. autofunction:: polf.line_xy(p0x: float, p0y: float, p1x: float, p1y: float, t: float) -> list

.. autofunction:: polf.cubic_bezier_xy(p0x: float, p0y: float, p1x: float, p1y: float, p2x: float, p2y: float, p3x: float, p3y: float, t: float) -> list

.. autofunction:: polf.quadratic_bezier_xy(p0x: float, p0y: float, p1x: float, p1y: float, p2x: float, p2y: float, t: float) -> list

.. autofunction:: polf.elliptical_arc_xy(p0x: float, p0y: float, rx: float, ry: float, x_axis_rotation: float, large_arc: bool, sweep: bool, p1x: float, p1y: float, t: float) -> list

