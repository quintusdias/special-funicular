class Grib2(object):
    def __init__(self, path):
        self.path = path

        self.parse()

    def parse(self):
        with self.path.open(mode='rb') as fp:
            self.parse_indicator_section(fp)

    def parse_indicator_section(self, fp):
        buffer = fp.read(16)
        if buffer[:4] != b'GRIB':
            msg = "Not a GRIB file"
            raise RuntimeError(msg)

        self.edition = buffer[7]


