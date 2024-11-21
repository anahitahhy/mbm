import cv2
import numpy as np
import os


def tile_image(input_image_path, output_dir, tile_size=100):
    os.makedirs(output_dir, exist_ok=True)

    # خواندن تصویر اصلی
    original_image = cv2.imread(input_image_path)

    # ایجاد 9 تصویر کاشی
    for i in range(3):
        for j in range(3):
            # محاسبه منطقه برش
            start_x = i * tile_size
            start_y = j * tile_size

            # برش منطقه مورد نظر
            tile = original_image[start_y:start_y + tile_size, start_x:start_x + tile_size]

            # ذخیره تصویر
            output_path = os.path.join(output_dir, f'tile_{i}_{j}.png')
            cv2.imwrite(output_path, tile)

    print(f"9 تصویر کاشی در {output_dir} ذخیره شدند")


def reconstruct_image(tiles_dir, output_path='reconstructed_image.png'):
    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            tile_path = os.path.join(tiles_dir, f'tile_{i}_{j}.png')
            tile = cv2.imread(tile_path)

            if tile is None:
                raise ValueError(f"خطا در بارگذاری تصویر {tile_path}")

            row.append(tile)
        tiles.append(row)

    # ترکیب کاشی‌ها
    rows = [np.concatenate(row_tiles, axis=1) for row_tiles in tiles]
    reconstructed_image = np.concatenate(rows, axis=0)

    # ذخیره تصویر بازسازی شده
    cv2.imwrite(output_path, reconstructed_image)
    print("تصویر بازسازی شده ذخیره گردید")


def main():
    """اجرای کامل فرآیند پردازش تصویر"""
    input_image = 'gu.png'
    output_tiles_directory = 'output_tiles'

    # برش تصویر به کاشی‌ها
    tile_image(input_image, output_tiles_directory)

    # بازسازی تصویر از کاشی‌ها
    reconstruct_image(output_tiles_directory)


if __name__ == "__main__":
    main()