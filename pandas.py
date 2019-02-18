import codecs

PANDA_FACE = "\N{PANDA FACE}"
PANDA_CODE = "__3f5600991c5645958bd36367d77d75d1"  # random UUID4


def pandas_decode(input, errors):
    s = codecs.decode(input, encoding="utf-8", errors=errors)
    s = s.replace(PANDA_FACE, PANDA_CODE)
    return s


def pandas_encode(input, errors):
    input = input.replace(PANDA_CODE, PANDA_FACE)
    b = codecs.encode(input, encoding="utf-8", errors=errors)
    return b


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        res = pandas_encode(input, errors)
        return res, len(input)

    def decode(self, input, errors='strict'):
        res = pandas_decode(input, errors)
        return res, len(input)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return pandas_encode(input, self.errors)


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return pandas_decode(input, self.errors)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(
        name='pandas',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    )


def search_function(name):
    if name == 'pandas':
        return getregentry()


codecs.register(search_function)
