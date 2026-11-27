# CUDA Error Helper

A small, dependency-free command-line tool that maps common CUDA setup errors to short troubleshooting guides.

> Unofficial community project. Not affiliated with or endorsed by NVIDIA. Guides are summaries based on NVIDIA's official documentation (linked in each guide). Always check the official docs for your exact CUDA version and OS.

## Why
Beginners hit the same CUDA setup errors again and again, and answers are scattered across many forum threads. This repo collects the most common ones in one place, with links to the official docs.

## Usage
Requires Python 3 only.

```bash
python3 src/fix.py --list
python3 src/fix.py "nvcc not found"
python3 src/fix.py "CUDA driver version is insufficient for CUDA runtime version"
```

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

The tests check that error messages map to the right guide. They do not verify the fixes on real GPU machines.

## Guides
| Error | Guide |
|---|---|
| `nvcc: command not found` | [guides/nvcc-not-found.md](guides/nvcc-not-found.md) |
| `CUDA driver version is insufficient for CUDA runtime version` | [guides/driver-version-insufficient.md](guides/driver-version-insufficient.md) |
| `no CUDA-capable device is detected` | [guides/no-cuda-capable-device.md](guides/no-cuda-capable-device.md) |
| CUDA installer failed | [guides/cuda-install-failed.md](guides/cuda-install-failed.md) |

## Data
`data/threads.csv` lists public NVIDIA Developer Forum threads (title and link only) that I used to decide which errors to cover. `src/categorize.py` groups them by error type.

## Limitations
- Guides are written from official documentation and have not been tested on every OS or GPU.
- Mostly Linux-focused. Windows, WSL and Jetson often differ.
- Small sample of forum threads, so this is a starting point, not a complete error catalogue.

## Contributing
Found a mistake or a missing error? Please open an issue or pull request.
