"""
This file contains the interface to libsemigroups Todd-Coxeter; see

https://libsemigroups.readthedocs.io/en/latest/_generated/libsemigroups__congruence__toddcoxeter.html#classlibsemigroups_1_1congruence_1_1_todd_coxeter

for further details.
"""

import cppyy
import libsemigroups_cppyy.detail as detail
import cppyy.ll as ll


def ToddCoxeter(t):
    if not isinstance(t, str):
        raise TypeError("invalid argument, expected a string, but found " + t)
    if t == "right":
        t = cppyy.gbl.libsemigroups.congruence_type.right
    elif t == "left":
        t = cppyy.gbl.libsemigroups.congruence_type.left
    elif t == "twosided":
        t = cppyy.gbl.libsemigroups.congruence_type.twosided
    else:
        raise ValueError(
            'invalid argument, expected one of "right", "left" and "twosided", but found '
            + '"'
            + t
            + '"'
        )

    tc_type = cppyy.gbl.libsemigroups.congruence.ToddCoxeter

    undef = ll.static_cast["size_t"](cppyy.gbl.libsemigroups.UNDEFINED)

    tc_type.__repr__ = lambda x: "<ToddCoxeter object {0} generator{1} and {2} pair{3} at {4}>".format(
        x.nr_generators() if x.nr_generators() != undef else "-",
        "s"[: x.nr_generators() != 1],
        x.nr_generating_pairs(),
        "s"[: x.nr_generating_pairs() != 1],
        hex(id(x)),
    )

    def wrap_strategy(*args):
        if len(args) == 1:
            return [args[0]], ""
        overload = "libsemigroups::congruence::ToddCoxeter::policy::strategy"
        if len(args) != 2:
            raise TypeError("invalid argument, expected 0 or 1 arguments")
            # The user enters 0 or 1 arguments here, even though 1 or 2 arguments
            # is actually given to this function
        if not isinstance(args[1], str):
            raise TypeError("invalid argument, expected a string or no argument")
        if args[1] == "felsch":
            return [args[0], tc_type.policy.strategy.felsch], overload
        elif args[1] == "hlt":
            return [args[0], tc_type.policy.strategy.hlt], overload
        elif args[1] == "random":
            return [args[0], tc_type.policy.strategy.random], overload
        else:
            raise ValueError(
                'invalid argument, expected one of "felsch", "hlt" and "random", but found '
                + '"'
                + args[1]
                + '"'
            )

    def wrap_standardize(*args):
        if len(args) == 1:
            return [None], ""
        # overload is the type of the parameter of the cpp overload
        overload = "libsemigroups::congruence::ToddCoxeter::order"
        if len(args) != 2:
            raise TypeError("invalid argument, expected exactly one argument")
        if not isinstance(args[1], str):
            raise TypeError("invalid argument, expected a string")
        if args[1] == "lex":
            return [args[0], tc_type.order.lex], overload
        elif args[1] == "shortlex":
            return [args[0], tc_type.order.shortlex], overload
        elif args[1] == "recursive":
            return [args[0], tc_type.order.recursive], overload
        else:
            raise ValueError(
                'invalid argument, expected one of "lex", "shortlex" and "recursive", but found '
                + '"'
                + arg[1]
                + '"'
            )

    def int_to_kind(self, n):
        if n == 0:
            return "left"
        elif n == 1:
            return "right"
        elif n == 2:
            return "twosided"
        else:
            assert False

    def int_to_strategy(self, n):
        if isinstance(n, cppyy.gbl.libsemigroups.congruence.ToddCoxeter):
            return n
        elif n == 0:
            return "hlt"
        elif n == 1:
            return "felsch"
        elif n == 2:
            return "random"
        else:
            assert False

    detail.wrap_overload_params_and_unwrap_return_value(
        tc_type, tc_type.strategy, wrap_strategy, int_to_strategy
    )

    detail.wrap_overload_params_and_unwrap_return_value(
        tc_type, tc_type.standardize, wrap_standardize, lambda self, x: x
    )

    detail.unwrap_return_value(tc_type, tc_type.kind, int_to_kind)
    detail.unwrap_return_value(
        tc_type, tc_type.class_index_to_word, lambda self, x: list(x)
    )

    return tc_type(t)
