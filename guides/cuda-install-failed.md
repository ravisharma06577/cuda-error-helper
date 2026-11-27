# CUDA installer failed

**Why:** Installer failures usually come from unmet prerequisites or a conflict with an earlier installation.

## Checklist
1. **GPU:** confirm the system has a CUDA-capable NVIDIA GPU.
2. **OS:** confirm your OS version is supported (see the CUDA Toolkit release notes).
3. **Compiler (Linux):** a compatible gcc must be installed. Install your distro's development tools if the installer complains.
4. **Conflicts:** do not mix installation methods (package manager vs runfile). Remove the old installation fully before switching. The Installation Guide has a section on handling conflicting installation methods.
5. **Driver:** from CUDA 13.4, install the driver separately before or after the Toolkit as described in the driver guide.
6. **Read the installer log** instead of guessing. Its location is listed in the Installation Guide for your OS.

## Sources
- CUDA Installation Guide for Linux: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
- CUDA Installation Guide for Windows: https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/
