# py-devnullaas

is a python library to discard data through <https://devnull-as-a-service.com>
and other DAAS endpoints.

## Installation

![section tbd](https://f.codl.fr/1807/construction-gif-056.gif)

## Usage

py-devnullaas provides `NullStream`, a file-like object to which you can write
`string`s or `bytes`...es. Whatever the plural of `bytes` is.

```python
from devnullaas import NullStream

devnull = NullStream()

password = 'hunter2'

devnull.write(password)
del password  # once it has been discarded remotely,
              # we can discard our local copy
```

### Endpoint configuration

By default, `NullStream` uses `https://devnull-as-a-service.com/dev/null`, but
you can specify any DAAS-compliant endpoint in the constructor:

```python
devnull = NullStream(endpoint="http://devnull.local/dev/null")
devnull.write('foobar')
```

> ⚠️ **Warning**: Discarding data with an untrusted endpoint may result in
> compromised data. Usage with untrusted endpoints is not recommended.

### Offline usage

`NullStream` can also be used offline by passing `None` as the endpoint. While
much faster, this does not ensure safe discarding of data and should only be
used in environments where no DAAS can be reached.

```python
devnull = NullStream(endpoint=None)
devnull.write('foobar')
# has it truly been discarded? 🤷 I dunno
```

## Disclaimer

While fully functional, this is a joke, and should not be taken seriously.
*Please* do not use this. *Please* especially do not use this in production. I
mean, if something like this somehow makes its way into production you have some
bigger problems to fix, but still.
