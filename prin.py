


from datetime import datetime


def wrap(func):
    print("warp", func)
    func_warp.append(func)

    def action(*args, **kwargs):
        result = func(*args, **kwargs)
        print("decorator wrapper", result)
        return result

    return action


def clock(func):
    print("clock", func)
    func_clock.append(func)

    def action(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        message = "Start: {0}\n, end: {1}\n{2}"
        print(message.format(start, end, end-start))
        return result

    return action


@wrap
@clock
def func():
    for i in range(0, 10000):
        print(i)


if __name__ == '__main__':
    print (func())
