from fp17.bcds1 import BCDS1Message


def test_simple():
    msg = BCDS1Message()
    assert 'clrn' in msg.errors

    msg.data['clrn'] = '123456'
    assert not msg.errors

    root = msg.generate_xml()
    BCDS1Message.validate_xml(root)
