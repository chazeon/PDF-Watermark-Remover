import pytest
import importlib  
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).parent

from remove import removeWatermark

sys.path.insert(0, str(TESTS_DIR.parent))

@pytest.mark.parametrize("ifname", [TESTS_DIR / "lorem.pdf"])
def test_removal(ifname):
    ofname = TESTS_DIR / ("%s.out.pdf" % (Path(ifname).stem,))
    removeWatermark(str(ifname), str(ofname))