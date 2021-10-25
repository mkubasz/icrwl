from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Page:
     domain: str
     url: str
     content_len: str
     status: int
     referer: str
     externals_count: int
     internals_count: int
     external_links: list[str] = field(default_factory=list)
     internal_links: list[str] = field(default_factory=list)
