import pytest
from ropey import Rope
from itertools import product, chain

TEXTS = [
    "I speak English",
    "Je parle français",
    "This should be a nice test since the sentence might a longer than the others",
    "This is\na\nmultiline\nstring",
]

LONG_TEXT_FILES = [
    "tests/data/short.txt",
    "tests/data/medium.txt",
    "tests/data/large.txt",
]


SLICES = [
    slice(None, None),
    slice(4, None),
    slice(None, 6),
    slice(3, 7),
]


def _p(py, rs, *args):
    """
    Generates arguments for test function.

    Test should assert that py(*arg) == rs(*arg)

    Note that arg != args
    """
    for arg in product(*args):
        yield py, rs, *arg


def _b(py, rs, *args):
    """
    Generates arguments for benchmark function.

    Test should assert that bench(*arg) == ref(*arg)

    Note that arg != args
    """
    return chain(_p(py, rs, *args, ["python"]), _p(rs, py, *args, ["rust"]))


def py_from_str(s):
    return s


def rs_from_str(s):
    return Rope.from_str(s).text


def py_len_chars(s):
    return len(s)


def rs_len_chars(s):
    return Rope.from_str(s).len_chars()


def py_len_lines(s):
    return len(s.splitlines())


def rs_len_lines(s):
    return Rope.from_str(s).len_lines()


def py_remove_range_full(s):
    return ""


def rs_remove_range_full(s):
    r = Rope.from_str(s)
    r.remove_range_full()
    return r.text


def py_remove(s, slc):
    start = slc.start or 0
    stop = slc.stop or len(s)
    return s[:start] + s[stop:]


def rs_remove(s, slc):
    r = Rope.from_str(s)
    r.remove(slc)
    return r.text


def py_split_off(s, char_idx):
    return s[char_idx:]


def rs_split_off(s, char_idx):
    r = Rope.from_str(s)
    return r.split_off(char_idx).text


def py_append(a, b):
    return a + b


def rs_append(a, b):
    r = Rope.from_str(a)
    r.append(Rope.from_str(b))
    return r.text


class TestRope:
    def test_new(self):
        r = Rope()

    @pytest.mark.parametrize("py,rs,text", _p(py_from_str, rs_from_str, TEXTS))
    def test_from_str(self, py, rs, text):
        assert py(text) == rs(text)

    @pytest.mark.parametrize(
        "bench,ref,file,_", _b(py_from_str, rs_from_str, LONG_TEXT_FILES)
    )
    def test_from_str_benchmark(self, bench, ref, file, _, benchmark):
        text = open(file).read()
        assert benchmark(bench, text) == ref(text)

    @pytest.mark.parametrize("py,rs,text", _p(py_len_chars, rs_len_chars, TEXTS))
    def test_len_chars(self, py, rs, text):
        assert py(text) == rs(text)

    @pytest.mark.parametrize("py,rs,text", _p(py_len_lines, rs_len_lines, TEXTS))
    def test_len_lines(self, py, rs, text):
        assert py(text) == rs(text)

    @pytest.mark.parametrize(
        "py,rs,text", _p(py_remove_range_full, rs_remove_range_full, TEXTS)
    )
    def test_remove_range_full(self, py, rs, text):
        assert py(text) == rs(text)

    @pytest.mark.parametrize("py,rs,text,slc", _p(py_remove, rs_remove, TEXTS, SLICES))
    def test_remove(self, py, rs, text, slc):
        assert py(text, slc) == rs(text, slc)

    @pytest.mark.parametrize(
        "py,rs,text,char_idx", _p(py_split_off, rs_split_off, TEXTS, [1, 2, 3, 4, 5])
    )
    def test_split_off(self, py, rs, text, char_idx):
        assert py(text, char_idx) == rs(text, char_idx)

    @pytest.mark.parametrize(
        "py,rs,text_a,text_b", _p(py_append, rs_append, TEXTS, TEXTS)
    )
    def test_append(self, py, rs, text_a, text_b):
        assert py(text_a, text_b) == rs(text_a, text_b)
