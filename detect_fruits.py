import json
from pathlib import Path
from typing import Dict

import click
import cv2
from tqdm import tqdm
# My import
import numpy as np


def detect_fruits(img_path: str) -> Dict[str, int]:
    """Fruit detection function, to implement.

    Parameters
    ----------
    img_path : str
        Path to processed image.

    Returns
    -------
    Dict[str, int]
        Dictionary with quantity of each fruit.
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # TODO: Implement detection method.
    # MY SCRIPT

    blur_value = 5
    # while True:

    blurred_frame = cv2.GaussianBlur(img, (blur_value, blur_value), 0)
    img_hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, (640, 480))
    img_hsv = cv2.resize(img_hsv, (640, 480))
    blurred_frame_img = cv2.resize(blurred_frame, (640, 480))
    # lower mask (0-10)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 250, 250])
    jablka_mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    jablka_mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([15, 100, 255])
    jablka_mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    # join my masks
    jablka_mask = jablka_mask0 + jablka_mask1

    # set my output img to zero everywhere except my mask
    jablka_output_img = img.copy()
    jablka_output_img[np.where(jablka_mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    jablka_output_hsv = img_hsv.copy()
    jablka_output_hsv[np.where(jablka_mask == 0)] = 0
    jablka_contours, _ = cv2.findContours(jablka_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    jablka_counter = 0
    # area = cv2.contourArea(contours)
    # print(area)

    for contour in jablka_contours:
        # area = cv2.contourArea(contour)
        # while area>1000:
        #     if area>1000:

        jablka_area = cv2.contourArea(contour)
        print(jablka_area)
        # while area>1000:
        if jablka_area > 1400:
            cv2.drawContours(jablka_mask, contour, -1, (0, 255, 0), 3)
            jablka_counter = jablka_counter + 1
    # END OF MY SCRIPT
    apple = jablka_counter
    banana = 0
    orange = 0
    orange_blur_value = 5
    # while True:
    # kernel = np.ones((blur_value, blur_value), np.float32) / 15
    # dst = cv2.filter2D(img, -1, kernel)
    orange_blurred_frame = cv2.GaussianBlur(img, (orange_blur_value, orange_blur_value), 0)
    orange_img_hsv = cv2.cvtColor(orange_blurred_frame, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, (640, 480))
    orange_img_hsv = cv2.resize(orange_img_hsv, (640, 480))
    orange = cv2.resize(orange_img_hsv, (640, 480))
    orange_blurred_frame_img = cv2.resize(orange_blurred_frame, (640, 480))
    # lower mask (0-10)
    lower_orange = np.array([10, 220, 10])
    upper_orange = np.array([15, 256, 256])
    orange_mask0 = cv2.inRange(orange_img_hsv, lower_orange, upper_orange)

    #     # upper mask (170-180)
    # lower_red = np.array([170, 50, 50])
    # upper_red = np.array([180, 255, 255])
    # jablka_mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    orange_mask = orange_mask0

    # set my output img to zero everywhere except my mask
    orange_output_img = img.copy()
    orange_output_img[np.where(orange_mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    orange_output_hsv = orange_img_hsv.copy()
    orange_output_hsv[np.where(orange_mask == 0)] = 0
    orange_contours, _ = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    orange_counter = 0
    # area = cv2.contourArea(contours)
    # print(area)

    for contour in orange_contours:
        # area = cv2.contourArea(contour)
        # while area>1000:
        #     if area>1000:

        orange_area = cv2.contourArea(contour)
        # print(orange_area)
        # while area>1000:
        if orange_area > 1400:
            cv2.drawContours(orange_mask, contour, -1, (0, 255, 0), 3)
            orange_counter = orange_counter + 1
    orange = orange_counter

    #Banana
    banana_blur_value = 5
    # while True:
    # kernel = np.ones((blur_value, blur_value), np.float32) / 15
    # dst = cv2.filter2D(img, -1, kernel)
    banana_blurred_frame = cv2.GaussianBlur(img, (banana_blur_value, banana_blur_value), 0)
    banana_img_hsv = cv2.cvtColor(banana_blurred_frame, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, (640, 480))
    banana_img_hsv = cv2.resize(banana_img_hsv, (640, 480))
    banana = cv2.resize(banana_img_hsv, (640, 480))
    banana_blurred_frame_img = cv2.resize(banana_blurred_frame, (640, 480))
    # lower mask (0-10)
    lower_yellow = np.array([25, 25, 10])
    upper_yellow = np.array([40, 256, 256])
    banana_mask0 = cv2.inRange(banana_img_hsv, lower_yellow, upper_yellow)

    #     # upper mask (170-180)
    # lower_red = np.array([170, 50, 50])
    # upper_red = np.array([180, 255, 255])
    # jablka_mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    banana_mask = banana_mask0

    # set my output img to zero everywhere except my mask
    banana_output_img = img.copy()
    banana_output_img[np.where(banana_mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    banana_output_hsv = banana_img_hsv.copy()
    banana_output_hsv[np.where(banana_mask == 0)] = 0
    banana_contours, _ = cv2.findContours(banana_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    banana_counter = 0
    # area = cv2.contourArea(contours)
    # print(area)

    for contour in banana_contours:
        # area = cv2.contourArea(contour)
        # while area>1000:
        #     if area>1000:

        banana_area = cv2.contourArea(contour)
        # print(orange_area)
        # while area>1000:
        if banana_area > 1400:
            cv2.drawContours(banana_mask, contour, -1, (0, 255, 0), 3)
            banana_counter = banana_counter + 1
    apple=jablka_counter
    banana=banana_counter
    orange=orange_counter
    return {'apple': apple, 'banana': banana, 'orange': orange}


@click.command()
@click.option('-p', '--data_path', help='Path to data directory', type=click.Path(exists=True, file_okay=False,
                                                                                  path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path),
              required=True)
def main(data_path: Path, output_file_path: Path):
    img_list = data_path.glob('*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        fruits = detect_fruits(str(img_path))
        results[img_path.name] = fruits

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)


if __name__ == '__main__':
    main()
