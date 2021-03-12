from playLA.Vector import Vector


if __name__ == '__main__':
    vec = Vector([5, 2])
    print(vec)
    print(vec.list, type(vec.list))
    print(type(vec))
    print('vec length：', len(vec))
    print('vec[0] = {}, vec[1] = {}'.format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print('{} + {} = {}'.format(vec, vec2, vec + vec2))
    print('{} - {} = {}'.format(vec, vec2, vec - vec2))

    print('{} * {} = {}'.format(vec, 5, vec * 5))
    print('{} * {} = {}'.format(5, vec, 5 * vec))

    print('+{} = {}'.format(vec, +vec))
    print('-{} = {}'.format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)
    print('{} + {} = {}'.format(vec, zero2, vec + zero2))

    print('vec.norm = {}'.format(vec.norm))
    print('vec2.norm = {}'.format(vec2.norm))

    print('vec.normalize is {}'.format(vec.normalize))
    print(vec.normalize.norm)

    try:
        zero2.normalize
    except ZeroDivisionError:
        print('Cannot normalize zero vector {}'.format(zero2))

    print('{}.dot({}) = {}'.format(vec, vec2, vec.dot(vec2)))
