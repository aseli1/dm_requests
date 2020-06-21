from .test_object import test_object, test_device
import vcr

dm = test_object


@vcr.use_cassette('tests/cassettes/device/all')
def test_all():
    response = dm.device.all()
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/device/details')
def test_details():
    response = dm.device.details(test_device['details_id'])
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/device/approve')
def test_approve():
    response = dm.device.approve(test_device['update_id'])
    assert response == 'Device approved'


@vcr.use_cassette('tests/cassettes/device/update')
def test_update():
    response = dm.device.update(
        test_device['update_id'], test_device['update_json'])
    assert response == 'Device updated'


@vcr.use_cassette('tests/cassettes/device/delete')
def test_delete():
    response = dm.device.delete(test_device['update_id'])
    assert response == 'Device deleted'
