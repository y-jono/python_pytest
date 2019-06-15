from acme.range import Range
import pytest

def test_上端点は下端点より大きい():
    with pytest.raises(TypeError) as errorInfo:
        _ = Range(1, 0)
    exceptionMessage = errorInfo.value.args[0]
    assert exceptionMessage == '上端よりおおきい下端は設定できません'

def test_上端と下端が一致する閉区間は等価と判定する():
    rangeX = Range(0, 1)
    rangeY = Range(0, 1)
    assert rangeX == rangeY

def test_上端が一致しない閉区間は等価にはならない():
    rangeX = Range(0, 1)
    rangeY = Range(0, 2)
    assert rangeX != rangeY

def test_下端が一致しない閉区間は等価にはならない():
    rangeX = Range(0, 3)
    rangeY = Range(2, 3)
    assert rangeX != rangeY
    
def test_文字列として表現できる():
    range = Range(3, 8)
    assert str(range) == "[3,8]"

def test_指定した整数を含むかどうかを判定できる():
    range = Range(0, 2)
    assert 1 in range

def test_別の区間を含むかどうかを判定できる():
    rangeX = Range(0, 3)
    rangeY = Range(1, 2)
    assert rangeY in rangeX
