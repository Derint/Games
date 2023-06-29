import sys
DEFAULT_TIMEOUT = 30.0
INTERVAL = 0.05

def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    m, s = '', ''
    t = ''
    if minutes:
        m = f'{minutes}' if minutes>9 else f'0{minutes}'
        t = ':'
    if seconds:
        s = f'{seconds}' if seconds>9 else f'0{seconds}'
        
    return "%s%s%s"%(m, t, s)

def backspace(len):
    print('\r' + ' '*len , end='')

    
SP = ' '
CR = '\r'
LF = '\n'
CRLF = CR + LF


class TimeoutOccurred(Exception):
    pass


def echo(string):
    sys.stdout.write(string)
    sys.stdout.flush()


def win_inputimeout(prompt='', timeout=DEFAULT_TIMEOUT):
    echo(prompt)
    begin = time.monotonic()
    end = begin + timeout
    line = ''

    while time.monotonic() < end:
        tmp_time = f'[#{convert(round(end-time.monotonic()))}]'
        tmp_time = tmp_time.ljust(len(tmp_time)+4)
        if msvcrt.kbhit():
            c = msvcrt.getwche()
            if c in (CR, LF):
                return line

            if c:return c
        time.sleep(INTERVAL)
        print(f'\r{prompt}{tmp_time}{line}', end='')

    echo(CRLF)
    raise TimeoutOccurred



try:
    import msvcrt

except ImportError:
    pass # for linux
else:
    import time
    inputimeout = win_inputimeout
