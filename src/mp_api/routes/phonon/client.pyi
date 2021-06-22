from typing import List, Optional
from mp_api.routes.phonon.models import PhononBSDoc, PhononImgDoc


class PhononRester:

    def get_document_by_id(
        self,
        document_id: str,
        fields: Optional[List[str]] = None,
        monty_decode: bool = True,
    ) -> PhononBSDoc: ...


class PhononImgRester:

    def get_document_by_id(
        self,
        document_id: str,
        fields: Optional[List[str]] = None,
        monty_decode: bool = True,
    ) -> PhononImgDoc: ...
