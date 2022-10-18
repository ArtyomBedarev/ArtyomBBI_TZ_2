def _min(args):
    m_min = float('inf')
    for i in args:
        if i < m_min:
            m_min = i
    return m_min


def _max(args):
    m_max = -float('inf')
    for i in args:
        if i > m_max:
            m_max = i
    return m_max


def _mult(args):
    m_mult = 1
    for i in args:
        m_mult *= i
    return m_mult


def _sum(args):
    m_sum = 0
    for i in args:
        m_sum += i
    return m_sum


