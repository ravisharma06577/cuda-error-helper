import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
import fix


class TestFix(unittest.TestCase):
    def test_guide_files_exist(self):
        for name in fix.KEYWORDS:
            self.assertTrue((fix.GUIDES_DIR / name).exists(), name)

    def test_matches(self):
        cases = {
            "nvcc not found": "nvcc-not-found.md",
            "nvcc: command not found": "nvcc-not-found.md",
            "nvidia-smi shows CUDA but nvcc not found": "nvcc-not-found.md",
            "CUDA driver version is insufficient for CUDA runtime version": "driver-version-insufficient.md",
            "no CUDA-capable device is detected": "no-cuda-capable-device.md",
            "CUDA_ERROR_NO_DEVICE": "no-cuda-capable-device.md",
            "Failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected": "no-cuda-capable-device.md",
            "CUDA installer failed": "cuda-install-failed.md",
        }
        for query, expected in cases.items():
            self.assertEqual(fix.best_match(query), expected, query)

    def test_unrelated_query_returns_none(self):
        self.assertIsNone(fix.best_match("something random xyz"))


if __name__ == "__main__":
    unittest.main()
