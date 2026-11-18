"""Hypothesis fuzz tests for the marathon registration parser."""
from hypothesis import given, strategies as st
from marathon_registration_parser import (
    format_bib_name, parse_finish_time, average_split,
)


@given(st.text() | st.none())
def test_format_bib_name_no_crash(s):
    try:
        result = format_bib_name(s)
    except Exception as exc:
        assert False, f"format_bib_name crashed on {s!r}: {exc}"
    assert isinstance(result, str)
    assert len(result) <= 12
    assert result == (s.strip().upper()[:12] if isinstance(s, str) else "")


@given(st.text() | st.none())
def test_parse_finish_time_no_crash(s):
    try:
        result = parse_finish_time(s)
    except Exception as exc:
        assert False, f"parse_finish_time crashed on {s!r}: {exc}"
    assert result is None or (isinstance(result, int) and result >= 0)
    if result is not None:
        h, m, sec = s.strip().split(":")
        assert h.isascii() and h.isdecimal()
        assert len(m) == len(sec) == 2
        assert 0 <= int(m) < 60 and 0 <= int(sec) < 60
        assert len(h) <= 100
        assert result == int(h) * 3600 + int(m) * 60 + int(sec)


@given(st.text() | st.none())
def test_average_split_no_crash(s):
    try:
        result = average_split(s)
    except Exception as exc:
        assert False, f"average_split crashed on {s!r}: {exc}"
    assert result is None or (isinstance(result, float) and result >= 0)
    if result is not None:
        parts = s.split()
        assert parts and all(p.isascii() and p.isdecimal() for p in parts)
        assert all(len(p) <= 100 for p in parts)
        assert result == sum(map(int, parts)) / len(parts)


def test_known_valid_inputs():
    assert format_bib_name("  rohit pujari  ") == "ROHIT PUJARI"
    assert parse_finish_time("3:45:10") == 13510
    assert average_split("25 26 24") == 25.0


def test_known_invalid_inputs():
    assert format_bib_name(None) == ""
    assert parse_finish_time("2:99:99") is None
    assert parse_finish_time("3:45") is None
    assert average_split("") is None
    assert average_split("25 abc") is None
