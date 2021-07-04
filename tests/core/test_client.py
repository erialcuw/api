import pytest
from mp_api.core.client import BaseRester
from mp_api.matproj import MPRester


@pytest.fixture
def rester():
    rester = BaseRester()
    yield rester
    rester.session.close()


@pytest.fixture()
def mpr():
    rester = MPRester()
    yield rester
    rester.session.close()


@pytest.mark.xfail
def test_post_fail(rester):
    rester._post_resource({}, suburl="materials/find_structure")


def test_pagination(mpr):
    mpids = mpr.materials.search_material_docs(
        all_fields=False, fields=["material_id"], num_chunks=2, chunk_size=1000
    )
    assert len(mpids) > 1000


def test_count(mpr):
    count = mpr.materials.count(
        dict(task_ids="mp-149", all_fields=False, fields="material_id", limit=1000)
    )
    assert count == 1


@pytest.mark.xfail
def test_get_document_no_id(mpr):
    mpr.materials.get_document_by_id(None)


@pytest.mark.xfail
def test_get_document_no_doc(mpr):
    mpr.materials.get_document_by_id("mp-1a")


def test_available_fields(rester, mpr):
    assert len(mpr.materials.available_fields) > 0
    assert rester.available_fields == ["Unknown fields."]