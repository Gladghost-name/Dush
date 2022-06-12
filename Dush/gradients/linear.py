def LinearGradient(x1: str = '0', y1: str = '0', x2: str = '1', y2: str = '0', color1: str = 'none',
                   color2: str = 'none') -> str:
    return f'QLinearGradient( x1:{x1} y1:{y1}, x2:{x2} y2:{y2}, stop:{x1} {color1}, stop:{x2} {color2});'
