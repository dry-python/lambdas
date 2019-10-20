    # Callable[[CenterProtocol[T]], T]
    def __getattr__(self, key: str) -> Callable[[object], T1]:
        return operator.attrgetter(key)
