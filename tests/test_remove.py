import pytest
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).parent

sys.path.insert(0, str(TESTS_DIR.parent))

from remove import removeWatermark


@pytest.mark.parametrize("ifname", [TESTS_DIR / "lorem.pdf"])
def test_removal(ifname):
    ofname = TESTS_DIR / ("%s.out.pdf" % (Path(ifname).stem,))
    removeWatermark(str(ifname), str(ofname))
