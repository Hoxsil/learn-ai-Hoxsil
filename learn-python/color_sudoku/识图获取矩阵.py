from PIL import Image
import subprocess
import numpy as np
import os
import cv2


FLODER_PATH = os.path.dirname(os.path.abspath(__file__))
EXE_PATH = os.path.join(FLODER_PATH, 'color_soduku.exe')
FLODER_PATH = os.path.join(FLODER_PATH, "图片丢这里")
DEBUG_IMG_PATH = os.path.join(FLODER_PATH, 'debug_image.png')

# 数行数，这个是 ai 写的，有点难
def detect_row_count(pil_img: Image.Image):
    img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    # 对每一行求平均亮度：白色线的行，平均值会明显更高
    row_bright = np.mean(gray, axis=1)

    # 找亮度峰值（白色横线）
    bright_thresh = 210  # 白色阈值，越白数值越接近255，可微调
    peaks = []
    for y in range(h):
        if row_bright[y] > bright_thresh:
            peaks.append(y)

    # 合并挨在一起的像素，同一条白线只算1条
    def cluster(vals, gap=10):
        if not vals:
            return []
        vals = sorted(vals)
        groups = [[vals[0]]]
        for v in vals[1:]:
            if v - groups[-1][-1] < gap:
                groups[-1].append(v)
            else:
                groups.append([v])
        return [int(np.mean(g)) for g in groups]

    line_clusters = cluster(peaks, gap=10)
    row_count = len(line_clusters) - 1
    return row_count


def board_to_matrix(img_path, color_threshold=40):
    # 打开原图，裁剪棋盘区域
    im = Image.open(img_path).convert("RGB")
    board_img = im.crop((50, 559, 669, 1175))

    grid_size = detect_row_count(board_img)

    w, h = board_img.size

    cell_w = int(w / grid_size)

    add_w = int(cell_w / 4)

    origin = int(w / (2 * grid_size))

    color_map = dict()   # key:基准rgb元组, value:编号
    matrix = []
    next_id = 1

    for row in range(grid_size):
        row_data = []
        for col in range(grid_size):
            # 当前格子的裁剪范围
            cx0 = origin + col * cell_w
            cy0 = origin + row * cell_w

            # 裁剪小格子，求区域RGB均值，抗噪
            cell = board_img.crop((cx0-add_w, cy0-add_w, cx0+add_w, cy0+add_w))
            arr = np.array(cell)
            rgb = tuple(np.mean(arr, axis=(0,1)).astype(int))

            # 模糊匹配：遍历已存颜色，看距离
            match_id = None
            for base_rgb, cid in color_map.items():
                dr = rgb[0] - base_rgb[0]
                dg = rgb[1] - base_rgb[1]
                db = rgb[2] - base_rgb[2]
                dist = np.sqrt(dr*dr + dg*dg + db*db)
                if dist < color_threshold:
                    match_id = cid
                    break
            if match_id is not None:
                row_data.append(match_id)
            else:
                color_map[rgb] = next_id
                row_data.append(next_id)
                next_id += 1
        matrix.append(row_data)

    return matrix

def matrix_to_cpp_input(matrix):
    n = len(matrix)
    lines = [str(n)]
    for row in matrix:
        line = " ".join(str(x) for x in row)
        lines.append(line)
    return "\n".join(lines) + "\n"

def get_answer(input_data):
    p = subprocess.Popen(
        [EXE_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        encoding="gbk"
    )
    stdout, stderr = p.communicate(input=input_data)
    stdout_list = stdout.split(r' \n')
    for x in stdout_list:
        print(x)

png_names = []
for filename in os.listdir(FLODER_PATH):
    if filename.lower().endswith(".jpg"):
        png_names.append(filename)

for filename in png_names:
    file_path = os.path.join(FLODER_PATH, filename)
    input_data = board_to_matrix(file_path, color_threshold=30)
    input_data = matrix_to_cpp_input(input_data)
    print("input_data:")
    print(input_data)
    get_answer(input_data)
    print()
