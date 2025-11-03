ESTADO_GLOBAL = {"debug": False}


def liga_debug():
    ESTADO_GLOBAL["debug"] = True


def desliga_debug():
    ESTADO_GLOBAL["debug"] = False


def f(x):
    if ESTADO_GLOBAL.get("debug"):
        print("debug:", x)
    return x


