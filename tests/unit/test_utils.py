from xpanse.utils import build_request_payload


def test_build_request_payload_default():
    request_data = None
    actual = build_request_payload(request_data=request_data)
    expected = {
        "json": {
            "request_data": {},
        },
    }

    assert actual == expected


def test_build_request_payload_payload_field():
    request_data = None
    actual = build_request_payload(request_data=request_data, payload_field="data")
    expected = {
        "data": {
            "request_data": {},
        },
    }

    assert actual == expected


def test_build_request_payload_request_data():
    request_data = {"simple_request_data": True}
    actual = build_request_payload(request_data=request_data)
    expected = {
        "json": {
            "request_data": {
                "simple_request_data": True,
            },
        },
    }

    assert actual == expected


def test_build_request_payload_filters():
    request_data = None
    actual = build_request_payload(request_data=request_data, filters=[{"field": "new1"}])
    expected = {
        "json": {
            "request_data": {
                "filters": [{"field": "new1"}],
            },
        },
    }

    assert actual == expected


def test_build_request_payload_existing_filters():
    request_data = {"filters": [{"field": "existing1"}, {"field": "existing2"}]}
    actual = build_request_payload(request_data=request_data, filters=[{"field": "new1"}])
    expected = {
        "json": {
            "request_data": {
                "filters": [{"field": "existing1"}, {"field": "existing2"}, {"field": "new1"}],
            },
        },
    }

    assert actual == expected


def test_build_request_payload_extra_payload_data():
    request_data = {"sort": {}}
    actual = build_request_payload(request_data=request_data, extra_request_data={"use_page_token": True})
    expected = {
        "json": {
            "request_data": {
                "sort": {},
                "use_page_token": True,
            },
        },
    }

    assert actual == expected


def test_build_request_payload_existing_json_kwargs():
    request_data = {"sort": {}}
    actual = build_request_payload(request_data=request_data,
                                   extra_request_data={"use_page_token": True},
                                   filters=[{"field": "new"}],
                                   json={"request_data": {"filters": [{"field": "existing"}]}})
    expected = {
        "json": {
            "request_data": {
                "sort": {},
                "filters": [{"field": "existing"}, {"field": "new"}],
                "use_page_token": True,
            },
        },
    }

    assert actual == expected
