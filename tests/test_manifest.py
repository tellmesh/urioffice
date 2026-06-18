from __future__ import annotations

from importlib.resources import as_file

from uri_control import CapabilityRegistry

import urioffice


def test_manifest_loads():
    with as_file(urioffice.manifest_path()) as path:
        registry = CapabilityRegistry.from_manifest_files([path])
    assert registry.manifests[0].scheme == "urioffice"
    assert len(registry.routes) == 5


def test_manifest_matches_routes():
    from uri_control.edge.runtime import Runtime

    rt = Runtime(config={"office": {"driver": "mock"}})
    urioffice.register(rt)
    assert len(rt.routes) == 5
    assert any(r.pattern.endswith("/writer/command/render") for r in rt.routes)
