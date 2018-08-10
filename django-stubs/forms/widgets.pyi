from collections import OrderedDict
from datetime import date, datetime, time
from decimal import Decimal
from itertools import chain
from typing import (Any, Callable, Dict, Iterator, List, Optional, Set, Tuple,
                    Type, Union)

from django.contrib.admin.filters import SimpleListFilter
from django.contrib.admin.options import (InlineModelAdmin, StackedInline,
                                          TabularInline)
from django.contrib.contenttypes.admin import GenericInlineModelAdminChecks
from django.contrib.contenttypes.forms import BaseGenericInlineFormSet
from django.core.files.base import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import FieldFile
from django.forms.fields import Field
from django.forms.models import ModelForm
from django.forms.renderers import EngineMixin
from django.utils.safestring import SafeText


class MediaOrderConflictWarning(RuntimeWarning): ...

class Media:
    def __init__(
        self,
        media: Optional[Type[Any]] = ...,
        css: Optional[Union[Dict[str, List[str]], Dict[str, Tuple[str]]]] = ...,
        js: Optional[Union[List[str], Tuple[str]]] = ...,
    ) -> None: ...
    def render(self) -> SafeText: ...
    def render_js(self) -> List[SafeText]: ...
    def render_css(self) -> chain: ...
    def absolute_path(self, path: str) -> str: ...
    def __getitem__(self, name: str) -> Media: ...
    @staticmethod
    def merge(
        list_1: Union[List[int], List[str], Tuple[str]],
        list_2: Union[List[int], List[str], Tuple[str]],
    ) -> Union[List[int], List[str]]: ...
    def __add__(self, other: Media) -> Media: ...

class MediaDefiningClass(type):
    def __new__(
        mcs: Type[MediaDefiningClass],
        name: str,
        bases: Tuple,
        attrs: Union[
            Dict[str, Any],
            Dict[
                str,
                Optional[Union[List[str], Tuple[str, str, str, str], int, str]],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    Dict[str, Tuple[str]],
                    List[Type[Union[StackedInline, TabularInline]]],
                    List[str],
                    str,
                ],
            ],
            Dict[str, Union[Callable, Dict[str, Tuple[str]], Type[Model], str]],
            Dict[
                str,
                Union[
                    Callable,
                    List[Type[InlineModelAdmin]],
                    List[str],
                    Tuple[str, str, str],
                    str,
                ],
            ],
            Dict[str, Union[Callable, List[Type[TabularInline]], bool, str]],
            Dict[str, Union[Callable, List[str], Type[Model], str]],
            Dict[
                str,
                Union[
                    Callable,
                    Tuple[str],
                    Type[Union[Model, ModelForm]],
                    int,
                    str,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    Type[
                        Union[
                            GenericInlineModelAdminChecks,
                            BaseGenericInlineFormSet,
                        ]
                    ],
                    str,
                ],
            ],
            Dict[str, Union[Callable, property, str]],
            Dict[
                str,
                Union[
                    Dict[Type[CharField], Dict[str, bool]],
                    Dict[str, List[str]],
                    List[Type[Union[StackedInline, TabularInline]]],
                    Tuple[
                        Tuple[
                            None,
                            Dict[
                                str,
                                Tuple[
                                    Tuple[str, str], Tuple[str, str, str, str]
                                ],
                            ],
                        ]
                    ],
                    str,
                ],
            ],
            Dict[
                str,
                Union[
                    Dict[Type[IntegerField], Dict[str, Type[NumberInput]]],
                    Type[Model],
                    str,
                ],
            ],
            Dict[
                str,
                Union[
                    Dict[str, Tuple[str]],
                    Tuple[
                        Tuple[str, Dict[str, Tuple[str]]],
                        Tuple[str, Dict[str, Tuple[str]]],
                    ],
                    Type[Union[Model, ModelForm]],
                    str,
                ],
            ],
            Dict[str, Union[List[Callable], str]],
            Dict[str, Union[List[Type[SimpleListFilter]], str]],
            Dict[str, Union[List[str], Tuple[str], Type[ModelForm], str]],
            Dict[str, Union[Type[Paginator], str]],
        ],
    ) -> Type[Any]: ...

class Widget:
    needs_multipart_form: bool = ...
    is_localized: bool = ...
    is_required: bool = ...
    supports_microseconds: bool = ...
    attrs: Dict[Any, Any] = ...
    def __init__(
        self,
        attrs: Optional[
            Union[Dict[str, None], Dict[str, Union[int, str]], Dict[str, float]]
        ] = ...,
    ) -> None: ...
    def __deepcopy__(
        self,
        memo: Union[
            Dict[
                int,
                Union[
                    Dict[Any, Any],
                    List[Union[List[Any], Field, Widget]],
                    Field,
                    Widget,
                ],
            ],
            Dict[
                int,
                Union[
                    List[Tuple[str, str]],
                    List[Union[List[Tuple[str, str]], Field, Widget]],
                    OrderedDict,
                    Field,
                    Widget,
                ],
            ],
        ],
    ) -> Widget: ...
    @property
    def is_hidden(self) -> bool: ...
    def subwidgets(
        self, name: str, value: None, attrs: Dict[str, bool] = ...
    ) -> Iterator[Dict[str, Optional[Union[Dict[str, bool], bool, str]]]]: ...
    def format_value(self, value: Any) -> Optional[str]: ...
    def get_context(
        self,
        name: str,
        value: Any,
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[Dict[str, Union[bool, Decimal, str]], bool, str]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Optional[Union[Dict[str, Union[float, int, str]], bool, str]],
            ],
        ],
        Dict[str, Dict[str, Union[Dict[str, None], List[str], bool, str]]],
        Dict[
            str,
            Dict[str, Union[Dict[str, Union[bool, str]], List[int], bool, str]],
        ],
        Dict[
            str,
            Dict[str, Union[Dict[str, Union[bool, str]], List[str], bool, str]],
        ],
        Dict[str, Dict[str, Union[Dict[str, str], bool, FieldFile, str]]],
    ]: ...
    def render(
        self,
        name: str,
        value: Any,
        attrs: Optional[Dict[str, Union[bool, str]]] = ...,
        renderer: Optional[EngineMixin] = ...,
    ) -> SafeText: ...
    def build_attrs(
        self,
        base_attrs: Union[
            Dict[str, Union[Decimal, str]],
            Dict[str, Union[float, str]],
            Dict[str, Union[int, str]],
        ],
        extra_attrs: Optional[Dict[str, Union[bool, str]]] = ...,
    ) -> Union[
        Dict[str, Union[bool, float, str]], Dict[str, Union[Decimal, int, str]]
    ]: ...
    def value_from_datadict(
        self, data: dict, files: Dict[str, SimpleUploadedFile], name: str
    ) -> Any: ...
    def value_omitted_from_data(
        self,
        data: Union[
            Dict[str, Optional[Union[List[int], date, int, str]]],
            Dict[str, Union[datetime, Decimal, int, str]],
        ],
        files: Dict[str, SimpleUploadedFile],
        name: str,
    ) -> bool: ...
    def id_for_label(self, id_: str) -> str: ...
    def use_required_attribute(self, initial: Any) -> bool: ...

class Input(Widget):
    attrs: Dict[Any, Any]
    input_type: str = ...
    template_name: str = ...
    def __init__(
        self,
        attrs: Optional[
            Union[Dict[str, None], Dict[str, Union[int, str]], Dict[str, float]]
        ] = ...,
    ) -> None: ...
    def get_context(
        self,
        name: str,
        value: Any,
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[Dict[str, Union[bool, Decimal, str]], bool, str]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Optional[Union[Dict[str, Union[float, int, str]], bool, str]],
            ],
        ],
        Dict[str, Dict[str, Union[Dict[str, str], List[int], bool, str]]],
        Dict[str, Dict[str, Union[Dict[str, str], List[str], bool, str]]],
        Dict[str, Dict[str, Union[Dict[str, str], bool, FieldFile, str]]],
    ]: ...

class TextInput(Input):
    attrs: Union[Dict[str, None], Dict[str, Union[int, str]]]
    is_localized: bool
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class NumberInput(Input):
    attrs: Union[
        Dict[str, Union[decimal.Decimal, str]],
        Dict[str, Union[float, str]],
        Dict[str, int],
    ]
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class EmailInput(Input):
    attrs: Dict[str, Union[bool, str]]
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class URLInput(Input):
    attrs: Dict[str, str]
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class PasswordInput(Input):
    attrs: Union[Dict[str, bool], Dict[str, str]]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    render_value: bool = ...
    def __init__(
        self, attrs: Optional[Dict[str, bool]] = ..., render_value: bool = ...
    ) -> None: ...
    def get_context(
        self,
        name: str,
        value: Optional[str],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Dict[
        str, Dict[str, Optional[Union[Dict[str, Union[bool, str]], bool, str]]]
    ]: ...

class HiddenInput(Input):
    attrs: Dict[str, str]
    choices: django.forms.models.ModelChoiceIterator
    is_localized: bool
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class MultipleHiddenInput(HiddenInput):
    attrs: Dict[str, str]
    choices: List[Tuple[str, str]]
    input_type: str
    is_required: bool
    template_name: str = ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[List[int], List[str]]],
        attrs: Optional[Dict[str, str]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[Dict[str, Union[Dict[Any, Any], bool, str]]],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, str],
                    List[Dict[str, Union[Dict[str, str], bool, str]]],
                    List[int],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, str],
                    List[Dict[str, Union[Dict[str, str], bool, str]]],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
    ]: ...
    def value_from_datadict(
        self,
        data: Union[
            Dict[str, List[str]],
            Dict[
                str,
                Tuple[
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                ],
            ],
        ],
        files: Dict[Any, Any],
        name: str,
    ) -> Union[
        List[str],
        Tuple[
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
            int,
        ],
    ]: ...
    def format_value(
        self, value: Optional[Union[List[int], List[str]]]
    ) -> Union[List[int], List[str]]: ...

class FileInput(Input):
    attrs: Union[Dict[str, bool], Dict[str, str]]
    is_required: bool
    input_type: str = ...
    needs_multipart_form: bool = ...
    template_name: str = ...
    def format_value(self, value: Optional[str]) -> None: ...
    def value_from_datadict(
        self,
        data: Union[Dict[str, None], Dict[str, bool], Dict[str, str]],
        files: Union[Dict[str, SimpleUploadedFile], Dict[str, str]],
        name: str,
    ) -> Optional[Union[SimpleUploadedFile, str]]: ...
    def value_omitted_from_data(
        self,
        data: Dict[str, str],
        files: Union[Dict[str, SimpleUploadedFile], Dict[str, str]],
        name: str,
    ) -> bool: ...

class ClearableFileInput(FileInput):
    attrs: Dict[str, str]
    is_required: bool
    clear_checkbox_label: Any = ...
    initial_text: Any = ...
    input_text: Any = ...
    template_name: str = ...
    def clear_checkbox_name(self, name: str) -> str: ...
    def clear_checkbox_id(self, name: str) -> str: ...
    def is_initial(self, value: Optional[Union[File, str]]) -> bool: ...
    def format_value(
        self, value: Optional[Union[File, str]]
    ) -> Optional[FieldFile]: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def value_from_datadict(
        self,
        data: Union[Dict[str, None], Dict[str, bool], Dict[str, str]],
        files: Union[Dict[str, SimpleUploadedFile], Dict[str, str]],
        name: str,
    ) -> Any: ...
    def use_required_attribute(
        self, initial: Optional[Union[FieldFile, str]]
    ) -> bool: ...
    def value_omitted_from_data(
        self,
        data: Dict[str, str],
        files: Union[Dict[str, SimpleUploadedFile], Dict[str, str]],
        name: str,
    ) -> bool: ...

class Textarea(Widget):
    attrs: Union[Dict[str, int], Dict[str, str]]
    is_required: bool
    template_name: str = ...
    def __init__(
        self, attrs: Optional[Union[Dict[str, int], Dict[str, str]]] = ...
    ) -> None: ...

class DateTimeBaseInput(TextInput):
    format_key: str = ...
    supports_microseconds: bool = ...
    format: Any = ...
    def __init__(
        self,
        attrs: Optional[Dict[str, Union[int, str]]] = ...,
        format: Optional[str] = ...,
    ) -> None: ...
    def format_value(
        self, value: Optional[Union[date, time, str]]
    ) -> Optional[str]: ...

class DateInput(DateTimeBaseInput):
    attrs: Dict[str, str]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class DateTimeInput(DateTimeBaseInput):
    attrs: Dict[Any, Any]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class TimeInput(DateTimeBaseInput):
    attrs: Dict[str, str]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class CheckboxInput(Input):
    attrs: Dict[str, str]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    check_test: Callable = ...
    def __init__(
        self,
        attrs: Optional[Dict[str, str]] = ...,
        check_test: Optional[Callable] = ...,
    ) -> None: ...
    def format_value(
        self, value: Optional[Union[int, str]]
    ) -> Optional[str]: ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[int, str]],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Dict[
        str, Dict[str, Optional[Union[Dict[str, Union[bool, str]], bool, str]]]
    ]: ...
    def value_from_datadict(
        self,
        data: Dict[str, Optional[Union[List[int], datetime, int, str]]],
        files: Dict[str, SimpleUploadedFile],
        name: str,
    ) -> bool: ...
    def value_omitted_from_data(
        self,
        data: Dict[str, Optional[Union[List[int], datetime, int, str]]],
        files: Dict[Any, Any],
        name: str,
    ) -> bool: ...

class ChoiceWidget(Widget):
    allow_multiple_selected: bool = ...
    input_type: Any = ...
    template_name: Any = ...
    option_template_name: Any = ...
    add_id_index: bool = ...
    checked_attribute: Any = ...
    option_inherits_attrs: bool = ...
    choices: Any = ...
    def __init__(
        self,
        attrs: Optional[Dict[str, Union[bool, str]]] = ...,
        choices: Union[
            Iterator[Any],
            List[List[Union[int, str]]],
            List[
                Union[
                    Tuple[
                        Union[List[Tuple[str, str]], str],
                        Union[List[Tuple[str, str]], str],
                    ],
                    Tuple[int, int],
                ]
            ],
            List[int],
            Tuple,
        ] = ...,
    ) -> None: ...
    def __deepcopy__(
        self,
        memo: Dict[
            int,
            Union[
                List[Tuple[str, str]],
                List[Union[List[Tuple[str, str]], Field, Widget]],
                OrderedDict,
                Field,
                Widget,
            ],
        ],
    ) -> ChoiceWidget: ...
    def subwidgets(
        self,
        name: str,
        value: Optional[List[str]],
        attrs: Dict[str, Union[bool, str]] = ...,
    ) -> None: ...
    def options(
        self,
        name: str,
        value: List[str],
        attrs: Dict[str, Union[bool, str]] = ...,
    ) -> None: ...
    def optgroups(
        self,
        name: str,
        value: List[str],
        attrs: Optional[Dict[str, Union[bool, str]]] = ...,
    ) -> Union[
        List[
            Tuple[
                None,
                List[Dict[str, Union[Dict[str, Union[bool, str]], int, str]]],
                int,
            ]
        ],
        List[Tuple[int, int, int]],
    ]: ...
    def create_option(
        self,
        name: str,
        value: Union[time, int, str],
        label: Union[int, str],
        selected: Union[Set[str], bool],
        index: int,
        subindex: Optional[int] = ...,
        attrs: Optional[Dict[str, Union[bool, str]]] = ...,
    ) -> Union[
        Dict[str, Union[Dict[Any, Any], bool, time, str]],
        Dict[str, Union[Dict[str, Union[bool, str]], Set[str], int, str]],
    ]: ...
    def get_context(
        self,
        name: str,
        value: Any,
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Tuple[
                            List[Dict[str, Union[Dict[Any, Any], bool, str]]],
                            int,
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Tuple[
                            List[Dict[str, Union[Dict[str, bool], bool, str]]],
                            int,
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Union[
                            Tuple[
                                None,
                                List[
                                    Dict[str, Union[Dict[Any, Any], bool, str]]
                                ],
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[str, Union[Dict[str, bool], bool, str]]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Tuple[
                            None,
                            List[
                                Dict[str, Union[Dict[Any, Any], time, int, str]]
                            ],
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Tuple[
                            None,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Dict[str, Union[bool, str]], int, str
                                    ],
                                ]
                            ],
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Tuple[
                            None,
                            List[
                                Dict[
                                    str,
                                    Union[Dict[str, bool], Set[str], int, str],
                                ]
                            ],
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Union[
                            Tuple[
                                None,
                                List[
                                    Dict[str, Union[Dict[str, bool], bool, str]]
                                ],
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[str, Union[Dict[Any, Any], bool, str]]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, str],
                    List[
                        Tuple[
                            None,
                            List[Dict[str, Union[Dict[str, str], int, str]]],
                            int,
                        ]
                    ],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, str],
                    List[
                        Union[
                            Tuple[
                                List[
                                    Dict[str, Union[Dict[str, str], bool, str]]
                                ],
                                int,
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Dict[str, Union[bool, str]],
                                            bool,
                                            str,
                                        ],
                                    ]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, str],
                    List[
                        Union[
                            Tuple[
                                None,
                                List[
                                    Dict[str, Union[Dict[str, str], bool, str]]
                                ],
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Dict[str, Union[bool, str]],
                                            bool,
                                            str,
                                        ],
                                    ]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
    ]: ...
    def id_for_label(self, id_: str, index: str = ...) -> str: ...
    def value_from_datadict(
        self, data: dict, files: Dict[Any, Any], name: str
    ) -> Optional[Union[List[str], int, str]]: ...
    def format_value(self, value: Any) -> List[str]: ...

class Select(ChoiceWidget):
    attrs: Dict[str, Union[bool, str]]
    choices: Union[
        List[List[Union[int, str]]],
        List[
            Union[
                Tuple[
                    Union[
                        List[Tuple[str, str]],
                        Tuple[Tuple[str, str], Tuple[str, str]],
                        str,
                    ],
                    Union[
                        List[Tuple[str, str]],
                        Tuple[Tuple[str, str], Tuple[str, str]],
                        str,
                    ],
                ],
                Tuple[int, Union[int, str]],
            ]
        ],
        django.forms.fields.CallableChoiceIterator,
        django.forms.models.ModelChoiceIterator,
    ]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...
    add_id_index: bool = ...
    checked_attribute: Any = ...
    option_inherits_attrs: bool = ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[List[int], List[str], int, str]],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Tuple[
                            List[Dict[str, Union[Dict[Any, Any], bool, str]]],
                            int,
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Union[
                            Tuple[
                                None,
                                List[
                                    Dict[str, Union[Dict[Any, Any], bool, str]]
                                ],
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[str, Union[Dict[str, bool], bool, str]]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Tuple[
                            None,
                            List[
                                Dict[str, Union[Dict[Any, Any], time, int, str]]
                            ],
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Tuple[
                            None,
                            List[
                                Dict[
                                    str,
                                    Union[Dict[str, bool], Set[str], int, str],
                                ]
                            ],
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Union[
                            Tuple[
                                None,
                                List[
                                    Dict[str, Union[Dict[str, bool], bool, str]]
                                ],
                                int,
                            ],
                            Tuple[
                                str,
                                List[
                                    Dict[str, Union[Dict[Any, Any], bool, str]]
                                ],
                                int,
                            ],
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, bool],
                    List[
                        Tuple[
                            List[Dict[str, Union[Dict[str, bool], bool, str]]],
                            int,
                            int,
                        ]
                    ],
                    List[str],
                    bool,
                    str,
                ],
            ],
        ],
    ]: ...
    def use_required_attribute(self, initial: Any) -> bool: ...

class NullBooleanSelect(Select):
    attrs: Dict[Any, Any]
    def __init__(self, attrs: None = ...) -> None: ...
    def format_value(self, value: Optional[Union[bool, str]]) -> str: ...
    def value_from_datadict(
        self,
        data: Dict[str, Union[bool, str]],
        files: Dict[Any, Any],
        name: str,
    ) -> Optional[bool]: ...

class SelectMultiple(Select):
    attrs: Dict[Any, Any]
    choices: Union[
        List[Tuple[str, Union[Tuple[Tuple[str, str], Tuple[str, str]], str]]],
        django.forms.models.ModelChoiceIterator,
    ]
    is_required: bool
    allow_multiple_selected: bool = ...
    def value_from_datadict(
        self,
        data: Union[
            Dict[str, Optional[Union[List[int], datetime, int, str]]],
            Dict[
                str,
                Tuple[
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                    int,
                ],
            ],
            Dict[str, Union[List[str], str]],
        ],
        files: Dict[Any, Any],
        name: str,
    ) -> Optional[Union[List[int], List[str], str]]: ...
    def value_omitted_from_data(
        self, data: Dict[str, str], files: Dict[Any, Any], name: str
    ) -> bool: ...

class RadioSelect(ChoiceWidget):
    attrs: Dict[str, str]
    choices: Union[
        List[Tuple[str, Union[Tuple[Tuple[str, str], Tuple[str, str]], str]]],
        List[int],
        django.forms.models.ModelChoiceIterator,
    ]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...

class CheckboxSelectMultiple(ChoiceWidget):
    attrs: Dict[str, str]
    choices: Union[
        List[
            Tuple[
                Union[Tuple[Tuple[str, str], Tuple[str, str]], str],
                Union[Tuple[Tuple[str, str], Tuple[str, str]], str],
            ]
        ],
        django.forms.models.ModelChoiceIterator,
    ]
    is_required: bool
    allow_multiple_selected: bool = ...
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...
    def use_required_attribute(self, initial: Optional[List[str]]) -> bool: ...
    def value_omitted_from_data(
        self, data: Dict[str, str], files: Dict[Any, Any], name: str
    ) -> bool: ...
    def id_for_label(self, id_: str, index: Optional[str] = ...) -> str: ...

class MultiWidget(Widget):
    attrs: Dict[Any, Any]
    template_name: str = ...
    widgets: List[django.forms.widgets.Widget] = ...
    def __init__(
        self,
        widgets: Union[List[Union[Type[TextInput], RadioSelect]], Tuple[Input]],
        attrs: Optional[Dict[str, str]] = ...,
    ) -> None: ...
    @property
    def is_hidden(self) -> bool: ...
    def get_context(
        self,
        name: str,
        value: Optional[
            Union[
                List[Union[List[str], str]],
                List[Union[date, time]],
                datetime,
                str,
            ]
        ],
        attrs: Optional[Dict[str, Union[bool, str]]],
    ) -> Union[
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[
                        Dict[Any, Any],
                        List[
                            Dict[
                                str, Optional[Union[Dict[Any, Any], bool, str]]
                            ]
                        ],
                        bool,
                        str,
                    ]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[
                        Dict[str, Union[bool, str]],
                        List[
                            Dict[
                                str,
                                Optional[
                                    Union[
                                        Dict[str, Union[bool, str]], bool, str
                                    ]
                                ],
                            ]
                        ],
                        bool,
                        str,
                    ]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[
                        Dict[str, Union[bool, str]],
                        List[
                            Union[
                                Dict[
                                    str,
                                    Optional[
                                        Union[
                                            Dict[str, Union[bool, str]],
                                            List[
                                                Dict[
                                                    str,
                                                    Optional[
                                                        Union[
                                                            Dict[
                                                                str,
                                                                Union[
                                                                    bool, str
                                                                ],
                                                            ],
                                                            bool,
                                                            str,
                                                        ]
                                                    ],
                                                ]
                                            ],
                                            bool,
                                            str,
                                        ]
                                    ],
                                ],
                                Dict[
                                    str,
                                    Union[
                                        Dict[str, Union[bool, str]],
                                        List[
                                            Tuple[
                                                None,
                                                List[
                                                    Dict[
                                                        str,
                                                        Union[
                                                            Dict[Any, Any],
                                                            bool,
                                                            str,
                                                        ],
                                                    ]
                                                ],
                                                int,
                                            ]
                                        ],
                                        bool,
                                        str,
                                    ],
                                ],
                            ]
                        ],
                        bool,
                        str,
                    ]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Optional[
                    Union[
                        Dict[str, str],
                        List[
                            Dict[
                                str, Optional[Union[Dict[str, str], bool, str]]
                            ]
                        ],
                        bool,
                        str,
                    ]
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Dict[
                            str,
                            Union[
                                Dict[Any, Any],
                                List[
                                    Tuple[
                                        None,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Dict[str, bool], bool, str
                                                ],
                                            ]
                                        ],
                                        int,
                                    ]
                                ],
                                List[str],
                                bool,
                                str,
                            ],
                        ]
                    ],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[Any, Any],
                    List[
                        Union[
                            Dict[
                                str,
                                Union[
                                    Dict[Any, Any],
                                    List[
                                        Dict[
                                            str,
                                            Union[Dict[Any, Any], bool, str],
                                        ]
                                    ],
                                    bool,
                                    str,
                                ],
                            ],
                            Dict[
                                str,
                                Union[
                                    Dict[str, bool],
                                    List[
                                        Tuple[
                                            None,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Dict[str, bool],
                                                        bool,
                                                        str,
                                                    ],
                                                ]
                                            ],
                                            int,
                                        ]
                                    ],
                                    List[str],
                                    bool,
                                    str,
                                ],
                            ],
                        ]
                    ],
                    bool,
                    str,
                ],
            ],
        ],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Union[bool, str]],
                    List[
                        Union[
                            Dict[
                                str,
                                Union[
                                    Dict[str, Union[bool, str]],
                                    List[
                                        Dict[
                                            str,
                                            Union[
                                                Dict[str, Union[bool, str]],
                                                bool,
                                                str,
                                            ],
                                        ]
                                    ],
                                    bool,
                                    str,
                                ],
                            ],
                            Dict[
                                str,
                                Union[
                                    Dict[str, Union[bool, str]],
                                    List[
                                        Tuple[
                                            None,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Dict[str, bool],
                                                        bool,
                                                        str,
                                                    ],
                                                ]
                                            ],
                                            int,
                                        ]
                                    ],
                                    List[str],
                                    bool,
                                    str,
                                ],
                            ],
                        ]
                    ],
                    bool,
                    str,
                ],
            ],
        ],
    ]: ...
    def id_for_label(self, id_: str) -> str: ...
    def value_from_datadict(
        self,
        data: Dict[str, Union[List[str], str]],
        files: Dict[Any, Any],
        name: str,
    ) -> Union[List[None], List[Union[List[str], str]]]: ...
    def value_omitted_from_data(
        self, data: Dict[str, str], files: Dict[Any, Any], name: str
    ) -> bool: ...
    def decompress(self, value: Any) -> None: ...
    media: Any = ...
    def __deepcopy__(
        self,
        memo: Union[
            Dict[
                int,
                Union[
                    List[Tuple[str, str]],
                    List[Union[List[Tuple[str, str]], Widget]],
                    OrderedDict,
                    Field,
                    Widget,
                ],
            ],
            Dict[
                int,
                Union[List[Union[Field, Widget]], OrderedDict, Field, Widget],
            ],
        ],
    ) -> MultiWidget: ...
    @property
    def needs_multipart_form(self) -> bool: ...

class SplitDateTimeWidget(MultiWidget):
    attrs: Dict[Any, Any]
    is_required: bool
    widgets: List[django.forms.widgets.DateTimeBaseInput]
    supports_microseconds: bool = ...
    template_name: str = ...
    def __init__(
        self,
        attrs: Optional[Dict[str, str]] = ...,
        date_format: Optional[str] = ...,
        time_format: Optional[str] = ...,
        date_attrs: Optional[Dict[str, str]] = ...,
        time_attrs: Optional[Dict[str, str]] = ...,
    ) -> None: ...
    def decompress(
        self, value: Optional[Union[datetime, str]]
    ) -> Union[List[None], List[Union[date, time]]]: ...

class SplitHiddenDateTimeWidget(SplitDateTimeWidget):
    attrs: Dict[Any, Any]
    is_required: bool
    widgets: List[django.forms.widgets.DateTimeBaseInput]
    template_name: str = ...
    def __init__(
        self,
        attrs: Optional[Dict[str, str]] = ...,
        date_format: None = ...,
        time_format: None = ...,
        date_attrs: Optional[Dict[str, str]] = ...,
        time_attrs: Optional[Dict[str, str]] = ...,
    ) -> None: ...

class SelectDateWidget(Widget):
    none_value: Any = ...
    month_field: str = ...
    day_field: str = ...
    year_field: str = ...
    template_name: str = ...
    input_type: str = ...
    select_widget: Any = ...
    date_re: Any = ...
    attrs: Any = ...
    years: Any = ...
    months: Any = ...
    year_none_value: Any = ...
    month_none_value: Any = ...
    day_none_value: Any = ...
    def __init__(
        self,
        attrs: None = ...,
        years: Optional[Union[Tuple[Union[int, str]], range]] = ...,
        months: None = ...,
        empty_label: Optional[Union[Tuple[str, str], str]] = ...,
    ) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def format_value(
        self, value: Optional[Union[date, str]]
    ) -> Union[Dict[str, None], Dict[str, Union[int, str]]]: ...
    def id_for_label(self, id_: str) -> str: ...
    def value_from_datadict(
        self, data: Dict[str, str], files: Dict[Any, Any], name: str
    ) -> Optional[str]: ...
    def value_omitted_from_data(
        self, data: Dict[str, str], files: Dict[Any, Any], name: str
    ) -> bool: ...
