import sys

if not getattr(sys, 'frozen', False):  # pyinstaller 실행 환경이 아니면
    from .pyhwpx import Hwp
else:
    # pyinstaller에서는 지연 import
    import types
    def _get_Hwp():
        from .pyhwpx import Hwp
        return Hwp

    sys.modules[__name__].Hwp = _get_Hwp()

from .version import __version__