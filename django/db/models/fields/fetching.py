from contextlib import contextmanager

from asgiref.local import Local


def FETCH_ONE(fetcher, instance, **kwargs):
    fetcher.fetch(instance)


def FETCH_PEERS(fetcher, instance, **kwargs):
    if instance._state.peers:
        instances = [
            peer
            for weakref_peer in instance._state.peers
            if (peer := weakref_peer()) is not None
        ]
        fetcher.fetch_many(instances)
    else:
        # Peers aren’t tracked for QuerySets returning a single instance
        fetcher.fetch(instance)


class LazyFieldAccess(Exception):
    """Blocked lazy access of a model field."""

    pass


def RAISE(fetcher, instance, **kwargs):
    klass = instance.__class__.__qualname__
    field_name = fetcher.field.name
    raise LazyFieldAccess(f"Lazy loading of {klass}.{field_name} blocked.")


_default = FETCH_ONE
_local = Local()


def set_default_fetching_mode(mode):
    global _default
    if not callable(mode):  # TODO: verify signature
        raise TypeError("mode must be callable.")
    _default = mode


@contextmanager
def lazy_mode(mode):
    if not callable(mode):  # TODO: verify signature
        raise TypeError("on_delete must be callable.")

    orig = getattr(_local, "mode", None)
    _local.mode = mode
    try:
        yield
    finally:
        if orig is None:
            del _local.mode
        else:
            _local.mode = orig


def get_fetching_mode():
    return getattr(_local, "mode", _default)
