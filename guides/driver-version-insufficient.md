# `CUDA driver version is insufficient for CUDA runtime version`

**Why:** Your installed NVIDIA driver is older than the minimum the CUDA Toolkit (used by your app or library) requires.

## Steps
1. Find your driver version:
   ```bash
   nvidia-smi
   ```
2. Check the minimum driver for your CUDA version (Linux, minor version compatibility):
   | CUDA Toolkit | Minimum driver |
   |---|---|
   | 11.x | >= 450 |
   | 12.x | >= 525 |
   | 13.x | >= 580 |

   Windows driver numbers differ. The exact numbers for each release are in the CUDA Toolkit Release Notes.
3. If your driver is lower, update the NVIDIA driver (see the Driver Installation Guide), then reboot.
4. Re-run your program or `deviceQuery`.

**Note:** From CUDA 13.4, the driver is no longer bundled with the Toolkit and must be installed separately.

**Docker/containers:** the container usually uses the host machine's driver, so check the driver version on the host.

## Sources
- CUDA Compatibility: https://docs.nvidia.com/deploy/cuda-compatibility/
- CUDA Toolkit Release Notes: https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/
