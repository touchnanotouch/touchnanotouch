import os
import math
from PIL import Image, ImageDraw

def harmonograph_points(params, num_points, width, height, margin=20):
    """Генерирует точки гармониографа (минималистичный вариант)"""
    points = []
    scale = min((width - 2 * margin) // 2, (height - 2 * margin) // 2)
    for i in range(num_points):
        t = i * 0.005  # чуть медленнее, чтобы кривая была длиннее и плавнее
        x = (
            math.sin(params['f1'] * t + params['p1']) * math.exp(-params['d1'] * t) +
            math.sin(params['f2'] * t + params['p2']) * math.exp(-params['d2'] * t)
        )
        y = (
            math.sin(params['f3'] * t + params['p3']) * math.exp(-params['d3'] * t) +
            math.sin(params['f4'] * t + params['p4']) * math.exp(-params['d4'] * t)
        )
        px = int(width // 2 + scale * x)
        py = int(height // 2 + scale * y)
        points.append((px, py))
    return points

def generate_harmonograph_frame(frame, total_frames, width=512, height=256, num_points=4000):
    """Генерирует один кадр минималистичной анимации гармониографа (без размытия)"""
    img = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(img)

    # Плавная анимация параметров гармониографа
    phase = 2 * math.pi * frame / total_frames
    params = {
        'f1': 2 + 0.15 * math.sin(phase),
        'f2': 3 + 0.12 * math.cos(phase * 0.8),
        'f3': 2 + 0.13 * math.cos(phase * 1.1),
        'f4': 3 + 0.14 * math.sin(phase * 1.3),
        'p1': 0,
        'p2': math.pi / 2 + 0.3 * math.sin(phase * 0.7),
        'p3': math.pi / 2 + 0.3 * math.cos(phase * 0.9),
        'p4': 0,
        'd1': 0.0015 + 0.0005 * math.sin(phase * 0.5),
        'd2': 0.0015 + 0.0005 * math.cos(phase * 0.6),
        'd3': 0.0015 + 0.0005 * math.sin(phase * 0.8),
        'd4': 0.0015 + 0.0005 * math.cos(phase * 0.4),
    }

    points = harmonograph_points(params, num_points, width, height)
    draw.line(points, fill=0, width=2)
    return img

def create_harmonograph_gif(output_path, num_frames=120, duration=60):
    frames = []
    for frame in range(num_frames):
        img = generate_harmonograph_frame(frame, num_frames)
        frames.append(img)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
        quality=100
    )

def main():
    create_harmonograph_gif('assets/minimal_harmonograph.gif', num_frames=540, duration=60)
    print("Гифка с минималистичным гармониографом создана в assets/minimal_harmonograph.gif")

if __name__ == '__main__':
    main()
