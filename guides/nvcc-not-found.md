# `nvcc: command not found`

**Typical symptom:** `nvidia-smi` works and shows a CUDA version, but `nvcc` is not found.

**Why:** `nvidia-smi` comes with the GPU driver. `nvcc` comes with the CUDA Toolkit. Having the driver does not mean the Toolkit is installed or on your PATH.

## Steps (Linux)
1. Check whether nvcc is on your PATH:
   ```bash
   which nvcc
   ```
2. Check whether the Toolkit is installed at all:
   ```bash
   ls /usr/local | grep cuda
   ```
3. **If you see a `cuda-XX.X` folder**, add it to your PATH (replace 12.4 with your version):
   ```bash
   export PATH=/usr/local/cuda-12.4/bin${PATH:+:${PATH}}
   export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
   ```
   To keep this after closing the terminal, add the same two lines to `~/.bashrc`, then run `source ~/.bashrc`.
4. **If there is no cuda folder**, the Toolkit is not installed. Install it using the official guide.
5. Verify:
   ```bash
   nvcc --version
   ```

**Jetson users:** the Toolkit comes through JetPack, so follow NVIDIA's Jetson/JetPack docs instead.

## Sources
- CUDA Quick Start Guide: https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html
- CUDA Installation Guide for Linux: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
