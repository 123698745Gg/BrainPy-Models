def generate(data,
             col1='**Parameter**',
             col2='**Init Value**',
             col3='**Unit**',
             col4='**Explanation**'):
    key_len = len(col1)
    val_len = len(col2)
    unit_len = len(col3)
    desc_len = len(col4)

    fdata = []
    lines = data.strip().split('\n')
    for line in lines:
        if line.strip():
            ss = line.strip().split()
            fdata.append((ss[0], ss[1], ss[2], ' '.join(ss[3:])))

    # get length
    for key, val, unit, desc in fdata:
        if len(key) > key_len:
            key_len = len(key)
        if len(val) > val_len:
            val_len = len(val)
        if len(unit) > unit_len:
            unit_len = len(unit)
        if len(desc) > desc_len:
            desc_len = len(desc)

    # generate header
    lines = []
    lines.append(f"    {'=' * key_len} {'=' * val_len} {'=' * unit_len} {'=' * desc_len}")
    line = f"    {col1}{' ' * (key_len - len(col1))} " + \
           f"{col2}{' ' * (val_len - len(col2))} " + \
           f"{col3}{' ' * (unit_len - len(col3))} " + \
           f'{col4}'
    lines.append(line)
    lines.append(f"    {'-' * key_len} {'-' * val_len} {'-' * unit_len} {'-' * desc_len}")

    # generate
    for i, (key, val, unit, desc) in enumerate(fdata):
        line = f"    {key}{' ' * (key_len - len(key))} " + \
               f"{val}{' ' * (val_len - len(val))} " + \
               f"{unit}{' ' * (unit_len - len(unit))} " + \
               f'{desc}'
        lines.append(line)
        if i + 1 != len(fdata):
            lines.append('')

    # generate ender
    lines.append(f"    {'=' * key_len} {'=' * val_len} {'=' * unit_len} {'=' * desc_len}")

    print('\n'.join(lines))


if __name__ == '__main__':
    generate('''
        g_max 0.1 \ Maximum conductance.
        E 0. \ Reversal potential.
        tau_decay 10. ms Time constant of decay.
        tau_s 10. ms Time constant of source neuron (i.e. pre-synaptic neuron)
        tau_t 10. ms Time constant of target neuron (i.e. post-synaptic neuron)
        w_min 0. \ Minimal possible synapse weight.
        w_max 20. \ Maximal possible synapse weight.
        delta_A_s 0.5 \ Change on source neuron traces elicited by a source neuron spike.
        delta_A_t 0.5 \ Change on target neuron traces elicited by a target neuron spike.
        mode 'vector' \ Data structure of ST members.
    ''')

