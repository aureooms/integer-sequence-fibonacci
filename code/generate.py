def generator ( ) :
    a = 0
    b = 1
    while True:
        yield a
        a += b
        yield b
        b += a

if __name__ == '__main__' :

    import os.path
    import sys
    from itertools import dropwhile, takewhile

    args = sys.argv[1:]

    fr = int(args[0])
    to = int(args[1])
    de = args[2]

    F = generator()

    enumerator = enumerate( F )

    _range = takewhile( lambda x : x[0] <= to , dropwhile( lambda x : x[0] < fr , enumerator ) )

    for n , f in _range :

        sn = str(n)
        sf = str(f)
        lf = len(sf)

        shortf = sf if lf <= 80 else sf[:77] + '...'

        print( sn , shortf )

        with open( os.path.join( de , str(n) ) , 'w' ) as p :
            p.write( sf + '\n' )
