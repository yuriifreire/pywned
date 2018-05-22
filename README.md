# Pwned

![logo](logo.jpg)

Check if you have an account that has been compromised in a data breach

This tool is based on [https://haveibeenpwned.com/](https://haveibeenpwned.com/)

# Quick start

```bash
$ pip install ppwned
```
or

```bash
$ python setup.py install
```

# Usage

You can import the library and use it in your project that way:

```python
>>> from pwned import check

>>> check(<email>)
```
Or just use it on the command line like this:

```bash
$ pwned <email>
```

# Dependencies

- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [requests](http://docs.python-requests.org/en/latest/)

