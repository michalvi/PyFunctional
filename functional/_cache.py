from six import StringIO


class Cache(object):

    def __init__(self, iterable, cached=None):
        if cached is None:
            cached = []

        if iterable is None:
            iterable = ()

        self._cached = cached
        self._iterator = iter(iterable)

    def __iter__(self):
        for x in self._cached:
            yield x

        for x in self._iterate_and_cache():
            yield x

    def _iterate_and_cache(self):
        for x in self._iterator:
            self._cached.append(x)
            yield x

    def __str__(self):
        stream = StringIO()
        stream.write('[')

        for x in self._cached:
            stream.write('{}, '.format(x))

        stream.write('...]')
        stream.seek(0)
        return stream.read()

    def __repr__(self):
        return 'Cache({!s})'.format(self)
