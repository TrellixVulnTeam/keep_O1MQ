import logging
import sys
import typing

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(auto_attribs=True)
class A:
    a: typing.List["A"]
    b: "B"


@attr.s(auto_attribs=True)
class B:
    a: A


if __name__ == "__main__":
    import logging
    import sys

    import attr

    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.info("%s", attr.fields(A).a.type)
    logging.info("%s", attr.fields(A).b.type)

    logging.info("%s", attr.resolve_types(A, globals(), locals()))
    logging.info("%s", attr.fields(A).a.type)
    logging.info("%s", attr.fields(A).b.type)
