import os
import math
from PIL import Image, ImageDraw

def generate_mandelbrot(path, width=512, height=256, max_iter=64):
    img = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            # Преобразование координат
            re = 3.5 * (x / width) - 2.5
            im = 2.0 * (y / height) - 1.0
            c = complex(re, im)
            z = 0
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            color = int(255 * (n / max_iter))
            draw.point([x, y], fill=color)
    img.save(path)

def generate_projects_graph_svg(path):
    # Минималистичный граф: vacsh <-> ZAMath
    svg = '''<svg width="320" height="180" viewBox="0 0 320 180" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="80" cy="90" r="32" stroke="#222" stroke-width="2" fill="#fff"/>
      <circle cx="240" cy="90" r="32" stroke="#222" stroke-width="2" fill="#fff"/>
      <text x="80" y="95" text-anchor="middle" font-size="18" fill="#222" font-family="monospace">vacsh</text>
      <text x="240" y="95" text-anchor="middle" font-size="18" fill="#222" font-family="monospace">ZAMath</text>
      <line x1="112" y1="90" x2="208" y2="90" stroke="#222" stroke-width="2"/>
    </svg>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

def main():
    os.makedirs('assets', exist_ok=True)
    generate_mandelbrot('assets/mandelbrot.png')
    generate_projects_graph_svg('assets/projects-graph.svg')

if __name__ == '__main__':
    main()
