class Screen(object):
    # 定义实例变量，外部仅可读，内部使用 _width 调用
    @property
    def width(self):
        return self._width

    # 使实例变量可在外部通过 width = value 操作赋值
    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('width must be a postive integer!')
        self._width = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('heigh must be a postive integer!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
