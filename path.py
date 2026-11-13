import json
from pathlib import Path as _Path

class Path(_Path):

    def write_text(self, data: str, encoding: str | None = 'utf-8', errors: str | None = None, newline: str | None = None):
        path = self.resolve()
        tmp = path.with_name(path.name + ".tmp")
        with open(tmp, "w", encoding=encoding, errors=errors, newline=newline) as f:
            n = f.write(data)
        tmp.replace(path)
        return n

    def read_text(self, encoding: str | None = 'utf-8-sig', errors: str | None = None, newline: str | None = None):
        with open(self.resolve(), "r", encoding=encoding, errors=errors, newline=newline) as f:
            return f.read()

    def write_json(self, data, encoding='utf-8', ensure_ascii=False, indent=4, default=None, **kwargs):
        path = self.resolve()
        tmp = path.with_name(path.name + ".tmp")
        with open(tmp, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent, default=default, **kwargs)
        tmp.replace(path)

    def read_json(self, encoding='utf-8-sig', **kwargs):
        with open(self.resolve(), "r", encoding=encoding) as f:
            return json.load(f, **kwargs)