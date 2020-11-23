# -*- coding: utf-8 -*-

import brainpy as bp
import brainpy.numpy as np

def get_HindmarshRose(a = 1., b = 3., c = 1., d = 5., r = 0.01, s = 4., V_rest = -1.6):
    """
    Hindmarsh-Rose neuron model.

    .. math::
        &\\frac{d V}{d t} = y - a V^3 + b V^2 - z + I

        &\\frac{d y}{d t} = c - d V^2 - y

        &\\frac{d z}{d t} = r (s (V - V_{rest}) - z)

    Args:
        a (float): Model parameter.
        b (float): Model parameter.
        c (float): Model parameter.
        d (float): Model parameter.
        r (float): Model parameter.
        s (float): Model parameter.
        V_rest (float): Membrane resting potential.

    Returns:
        bp.NeuType: return description of Hindmarsh-Rose neuron model.

    References:
        .. [1] Hindmarsh, James L., and R. M. Rose. "A model of neuronal bursting using 
               three coupled first order differential equations." Proceedings of the 
               Royal society of London. Series B. Biological sciences 221.1222 (1984): 
               87-102.
        .. [2] Storace, Marco, Daniele Linaro, and Enno de Lange. "The Hindmarsh–Rose 
               neuron model: bifurcation analysis and piecewise-linear approximations." 
               Chaos: An Interdisciplinary Journal of Nonlinear Science 18.3 (2008): 
               033128.
    """

    ST = bp.types.NeuState(
        {'V':-1.6, 'y':-10., 'z':0., 'input': 0}
    )

    @bp.integrate
    def int_V(V, _t_, y, z, I_ext):
        return y - a * V * V * V + b * V * V - z + I_ext

    @bp.integrate
    def int_y(y, _t_, V):
        return c - d * V * V - y

    @bp.integrate
    def int_z(z, _t_, V):
        return r * (s * (V - V_rest) - z)
    
    def update(ST, _t_):
        V = int_V(ST['V'], _t_, ST['y'], ST['z'], ST['input'])
        y = int_y(ST['y'], _t_, ST['V'])
        z = int_z(ST['z'], _t_, ST['V'])
        ST['V'] = V
        ST['y'] = y
        ST['z'] = z
    
    def reset(ST):
        ST['input'] = 0
    
    return bp.NeuType(name="HindmarshRose_neuron",
                            requires=dict(ST=ST),
                            steps=(update, reset),
                            vector_based=False)
