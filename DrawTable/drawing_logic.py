"""Small, dependency-free helpers for deciding which drawing segments to render."""


def get_drawing_segments(fingertips, previous_point, drawing):
    """Return line segments and the next single-hand anchor.

    With one detected fingertip, connect consecutive frames to make a freehand
    stroke. With two fingertips, connect the two hands directly for that frame.
    Switching to two hands (or losing all hands) clears the single-hand anchor,
    preventing accidental lines between unrelated points.
    """
    if not drawing or not fingertips:
        return [], None

    if len(fingertips) >= 2:
        return [(fingertips[0], fingertips[1])], None

    current_point = fingertips[0]
    if previous_point is None:
        return [], current_point

    return [(previous_point, current_point)], current_point
