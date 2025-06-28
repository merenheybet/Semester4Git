import matplotlib.pyplot as plt
import ipywidgets as iw
from IPython.display import display


def de_casteljau_plot(P):
    """Draw all polygons in the de Casteljau pyramid of P for varying t.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than or equal to 1.
    """
    from bezier import de_casteljau_step

    assert len(P) > 0

    n = len(P)
    t = 0.3
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    lines = ax.plot(P[:, 0], P[:, 1], "o-")
    Q = P.copy()
    for i in range(n - 1):
        Q = de_casteljau_step(Q, t)
        [line] = ax.plot(Q[:, 0], Q[:, 1], "o-")
        lines.append(line)
    ax.grid(True)

    fig.subplots_adjust(left=0.25, bottom=0.25)

    fig_handle = display(fig, display_id=True)

    def redraw(t):
        Q = P.copy()
        for i in range(n - 1):
            Q = de_casteljau_step(Q, t)
            lines[i + 1].set_xdata(Q[:, 0])
            lines[i + 1].set_ydata(Q[:, 1])
        fig_handle.update(fig)

    iw.interact(redraw, t=(0.0, 1.0, 0.05))


def bezier1_plot(P):
    """Draw different Bezier curve approximations for the given P.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.
    """
    assert len(P) > 1

    from bezier import bezier1

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    B1 = bezier1(P.copy(), 10)

    [line0] = ax.plot(P[:, 0], P[:, 1], "o-", label="P")
    [line1] = ax.plot(B1[:, 0], B1[:, 1], "o-", label="bezier1")
    ax.legend(shadow=True)
    ax.grid(True)

    fig.subplots_adjust(left=0.25, bottom=0.25)

    fig_handle = display(fig, display_id=True)

    def redraw(m):
        B1 = bezier1(P.copy(), m)
        line1.set_xdata(B1[:, 0])
        line1.set_ydata(B1[:, 1])
        fig_handle.update(fig)

    iw.interact(redraw, m=(2, 70, 1))


def bezier2_plot(P):
    """Draw different Bezier curve approximations for the given P.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.
    """
    assert len(P) > 1

    from bezier import bezier2

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    B1 = bezier2(P.copy(), 1)

    [line0] = ax.plot(P[:, 0], P[:, 1], "o-", label="P")
    [line1] = ax.plot(B1[:, 0], B1[:, 1], "o-", label="bezier2")
    ax.legend(shadow=True)
    ax.grid(True)

    fig.subplots_adjust(left=0.25, bottom=0.25)

    fig_handle = display(fig, display_id=True)

    def redraw(depth):
        B1 = bezier2(P.copy(), depth)
        line1.set_xdata(B1[:, 0])
        line1.set_ydata(B1[:, 1])
        fig_handle.update(fig)

    iw.interact(redraw, depth=(0, 6, 1))
