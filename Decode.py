"""
这是解码idx文件的文件
"""
import numpy as np
import struct

class Decode:
    @classmethod
    def idx3_ubyte(cls, idx3_ubyte_file):
        print('正在解码idx3图片文件:', idx3_ubyte_file)
        bin_data = open(idx3_ubyte_file, 'rb').read()

        offset = 0
        fmt_header = '>iiii'
        magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
        print('魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols))

        image_size = num_rows * num_cols
        offset += struct.calcsize(fmt_header)
        fmt_image = '>' + str(image_size) + 'B'
        images = np.empty((num_images, num_rows, num_cols))
        for i in range(num_images):
            images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
            offset += struct.calcsize(fmt_image)

        print('解码完成')
        return images

    @classmethod
    def idx1_ubyte(cls, idx1_ubyte_file):
        print('正在解码idx1标签文件:', idx1_ubyte_file)
        bin_data = open(idx1_ubyte_file, 'rb').read()

        offset = 0
        fmt_header = '>ii'
        magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
        print('魔数:%d, 标签数量: %d张' % (magic_number, num_images))

        offset += struct.calcsize(fmt_header)
        fmt_image = '>B'
        labels = np.empty(num_images)
        for i in range(num_images):
            labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
            offset += struct.calcsize(fmt_image)

        print('解码完成')
        return labels
