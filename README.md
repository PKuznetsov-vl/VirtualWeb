# pyvirtualcam

pyvirtualcam sends frames to a virtual camera from Python.

## Usage


```
main.exe rtsp://10.16.66.223:522
```

<p align="center">
<img width="500" src="https://raw.githubusercontent.com/letmaik/pyvirtualcam/main/examples/screencasts/simple.gif">
</p>
    
pyvirtualcam uses the first available virtual camera it finds (see later section).

For more examples, including using different pixel formats like BGR, or selecting a specific camera device, check out the [`examples/`](https://github.com/letmaik/pyvirtualcam/tree/main/examples) folder.

See also the [API Documentation](https://letmaik.github.io/pyvirtualcam).

## Installation

### Windows: OBS

[OBS](https://obsproject.com/) includes a built-in virtual camera for Windows (since 26.0).

Install OBS virtual camera [install OBS](https://obsproject.com/).

Note that OBS provides a single camera instance only, so it is *not* possible to send frames from Python to the built-in OBS virtual camera, capture the camera in OBS, mix it with other content, and output it again to OBS' built-in virtual camera. To achieve such a workflow, use another virtual camera from Python (like Unity Capture) so that OBS' built-in virtual camera is free for use in OBS.


### macOS: OBS

[OBS](https://obsproject.com/) includes a built-in virtual camera for macOS (since 26.1).

**NOTE**: Starting with pyvirtualcam 0.10, only OBS 28 is supported. Install an older version if you need OBS 26 / 27 support.

To use the OBS virtual camera, follow these one-time setup steps:
- [Install OBS](https://obsproject.com/).
- Start OBS.
- Click "Start Virtual Camera" (bottom right), then "Stop Virtual Camera".
- Close OBS.

Note that OBS provides a single camera instance only, so it is *not* possible to send frames from Python, capture the camera in OBS, mix it with other content, and output it again as virtual camera.

### Linux: v4l2loopback

pyvirtualcam uses [v4l2loopback](https://github.com/umlaeute/v4l2loopback) virtual cameras on Linux.

To create a v4l2loopback virtual camera on Ubuntu, run the following:

```sh
sudo apt install v4l2loopback-dkms
sudo modprobe v4l2loopback devices=1
```

For further information, see the [v4l2loopback documentation](https://github.com/umlaeute/v4l2loopback).
