from __future__ import annotations

from uri_control.edge.runtime import Runtime

import urioffice


def test_status_mock():
    rt = Runtime(config={"office": {"driver": "mock"}})
    urioffice.register(rt)
    res = rt.call("urioffice://local/query/status", {}, {"params": {"host": "local"}})
    assert res["ok"]
    assert res["result"]["driver"] == "mock"


def test_writer_render_mock():
    rt = Runtime(config={"office": {"driver": "mock"}})
    urioffice.register(rt)
    res = rt.call(
        "urioffice://local/writer/command/render",
        {"title": "demo", "text": "Hello office", "format": "txt"},
        {"approved": True, "params": {"host": "local"}},
    )
    assert res["ok"]
    assert res["result"]["rendered"] is True
