from datetime import datetime
import time, threading


def kraken_limit(cmax, decrease):
    lock = threading.Lock()

    def decorate(func):
        counter = [0]
        lastTimeCalled = [0.0]

        def rateLimitedFunction(args, *kargs):
            counter[0] += 1
            print('counter: {} {}'.format(counter[0], counter[0] > cmax))
            lock.acquire()
            elapsed = time.clock() - lastTimeCalled[0]
            if counter[0] >= cmax:
                leftToWait = decrease - elapsed
            else:
                leftToWait = 0
            if leftToWait > 0 or counter[0] > cmax:
                print('leftToWait: {}'.format(leftToWait))
                time.sleep(leftToWait)
                counter[0] -= 1

            lock.release()

            ret = func(args, *kargs)
            lastTimeCalled[0] = time.clock()
            return ret

        return rateLimitedFunction

    return decorate


@kraken_limit(5, 2)
def print_test(st):
    print(st)
    print(datetime.utcnow())


for i in range(1, 15):
    print_test('toto')
