class requestlib():
    def _requests(self, _target, *_auth):
        _req = requests.get(
                            _target,
                            auth=_auth)
        if _req.status_code == 200:
            return _req