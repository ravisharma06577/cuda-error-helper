# `no CUDA-capable device is detected` (CUDA_ERROR_NO_DEVICE)

**Why:** CUDA cannot see a usable NVIDIA GPU. Common reasons: no NVIDIA GPU, driver not installed or loaded, or the GPU is not exposed to your environment (VM, container, WSL).

## Steps
1. Does the machine have an NVIDIA GPU? On Linux:
   ```bash
   lspci | grep -i nvidia
   ```
2. Does the driver work?
   ```bash
   nvidia-smi
   ```
   If this fails, install the NVIDIA driver and **reboot** so it loads.
3. Check that you are not hiding the GPU:
   ```bash
   echo $CUDA_VISIBLE_DEVICES
   ```
   An empty-but-set or wrong value can make CUDA see no devices.
4. Running in a VM, Docker or WSL? The GPU must be passed through to that environment. Check that environment's NVIDIA instructions.

## Sources
- CUDA Installation Guide for Linux (pre-installation: verify you have a CUDA-capable GPU): https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
