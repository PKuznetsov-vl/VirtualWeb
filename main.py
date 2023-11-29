import argparse
import logging
import sys

import pyvirtualcam
import cv2
from retry import retry

logging.basicConfig(level=logging.INFO,
                    #filename="logs.log", filemode="w",
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler("logs.log"), logging.StreamHandler(sys.stdout)])
logger = logging.getLogger()



@retry(Exception, delay=30, tries=3, logger=logger)
def connect_cam(RTSP_URL):
    cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        logging.error('Cannot open RTSP stream')
        raise Exception('Frame error')

    with pyvirtualcam.Camera(width=1280, height=720, fps=120) as cam:
        logging.info(f'Using virtual camera: {cam.device}')
        # frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
        while True:
            bool_op, frame = cap.read()
            cam.send(frame)

            cam.sleep_until_next_frame()
            if cv2.waitKey(1) == 27:
                break
            if not bool_op:
                logging.warning('Frame error')
                raise Exception('Frame error')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='VrCam',
        description='Convert RTSP to Virtual Cam')
    logging.info(f'Service started')
    parser.add_argument('RTSP')
    args = parser.parse_args()
    #'rtsp://admin:v1sionlabs@10.16.6.231:554/RVi/1/1'
    connect_cam(RTSP_URL=args.RTSP)
