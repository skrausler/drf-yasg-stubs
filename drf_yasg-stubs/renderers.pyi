from typing import Any, Optional, List

from rest_framework.renderers import BaseRenderer

from drf_yasg.codecs import _OpenAPICodec


class _SpecRenderer(BaseRenderer):
    validators: List[str] = ...   # XXX unused?
    codec_class: _OpenAPICodec = ...
    @classmethod
    def with_validators(cls, validators: List[str]): ...

class OpenAPIRenderer(_SpecRenderer): ...

class SwaggerJSONRenderer(_SpecRenderer): ...

class SwaggerYAMLRenderer(_SpecRenderer): ...

class _UIRenderer(BaseRenderer):
    template: str = ...
    def set_context(self, renderer_context: Any, swagger: Optional[Any] = ...) -> None: ...
    def resolve_url(self, to: Any): ...
    def get_auth_urls(self): ...
    def get_oauth2_config(self): ...

class SwaggerUIRenderer(_UIRenderer):
    def get_swagger_ui_settings(self): ...

class ReDocRenderer(_UIRenderer):
    def get_redoc_settings(self): ...

class ReDocOldRenderer(ReDocRenderer): ...
