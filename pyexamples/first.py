
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
off_x = 6
off_y = 6
d = h = 32
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv('1st', s_filer='', n_filer='', offset="(0,0,0)", to="(0,0,0)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('2nd', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(1st-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('3rd', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(2nd-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('4th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(3rd-east)", width=1, height=h, depth=d,
            caption=" "),

    # split

    to_Conv('5th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(4th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('5th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},-{off_y},0)", to="(4th-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),

    to_Conv('6th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(5th-east)", width=1, height=h, depth=d,
            caption=" ", color='ConvColor'),
    to_Conv('6th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(5th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),

    to_Conv('7th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(6th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('7th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(6th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),

    to_Conv('8th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(7th-east)", width=1, height=h, depth=d,
            caption=" ",color='ConvColor'),
    to_Conv('8th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(7th_1-east)", width=2, height=h/2, depth=d/2,
            caption=" ",color='2ConvColor'),

    # split

    to_Conv('9th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(8th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('9th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(8th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('9th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},-{off_y},0)", to="(8th_1-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),

    to_Conv('10th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(9th-east)", width=1, height=h, depth=d,
            caption=" ", color='ConvColor'),
    to_Conv('10th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(9th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('10th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(9th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),

    to_Conv('11th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(10th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('11th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(10th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('11th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(10th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),

    to_Conv('12th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(11th-east)", width=1, height=h, depth=d,
            caption=" ",color='ConvColor'),
    to_Conv('12th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(11th_1-east)", width=2, height=h/2, depth=d/2,
            caption=" ",color='2ConvColor'),
    to_Conv('12th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(11th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),

    # split

    to_Conv('13th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(12th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('13th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(12th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('13th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(12th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),
    to_Conv('13th_3', s_filer='', n_filer='', offset=f"({off_x-1.5},-{off_y},0)", to="(12th_2-east)", width=8, height=h / 8,
            depth=d / 8,
            caption=" ", color='4ConvColor'),

    to_Conv('14th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(13th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('14th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(13th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('14th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(13th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),
    to_Conv('14th_3', s_filer='', n_filer='', offset=f"({off_x-1.5},0,0)", to="(13th_3-east)", width=8, height=h / 8,
            depth=d / 8,
            caption=" ", color='4ConvColor'),

    to_Conv('15th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(14th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('15th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(14th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('15th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(14th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),
    to_Conv('15th_3', s_filer='', n_filer='', offset=f"({off_x-1.5},0,0)", to="(14th_3-east)", width=8, height=h / 8,
            depth=d / 8,
            caption=" ", color='4ConvColor'),


    to_Conv('16th', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(15th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('16th_1', s_filer='', n_filer='', offset=f"({off_x-0.25},0,0)", to="(15th_1-east)", width=2, height=h / 2,
            depth=d / 2,
            caption=" ", color='2ConvColor'),
    to_Conv('16th_2', s_filer='', n_filer='', offset=f"({off_x-0.75},0,0)", to="(15th_2-east)", width=4, height=h / 4,
            depth=d / 4,
            caption=" ", color='3ConvColor'),
    to_Conv('16th_3', s_filer='', n_filer='', offset=f"({off_x-1.5},0,0)", to="(15th_3-east)", width=8, height=h / 8,
            depth=d / 8,
            caption=" ", color='4ConvColor'),

    # concat

    to_Conv('out', s_filer='', n_filer='', offset=f"({off_x},0,0)", to="(16th-east)", width=1, height=h, depth=d,
            caption=" "),
    to_Conv('out_1', s_filer='', n_filer='', offset=f"(0,0,0)", to="(out-east)", width=2, height=h,
            depth=d,
            caption=" ", color='2ConvColor'),
    to_Conv('out_2', s_filer='', n_filer='', offset=f"(0,0,0)", to="(out_1-east)", width=4, height=h,
            depth=d,
            caption=" ", color='3ConvColor'),
    to_Conv('out_3', s_filer='', n_filer='', offset=f"(0,0,0)", to="(out_2-east)", width=8, height=h,
            depth=d,
            caption=" ", color='4ConvColor'),

    # horizontal
    to_connection('1st','2nd'),
    to_connection('2nd','3rd'),
    to_connection('3rd','4th'),
    to_connection('4th','5th'),
    to_connection('5th','6th'),
    to_connection('6th','7th'),
    to_connection('7th','8th'),
    to_connection('8th','9th'),
    to_connection('9th','10th'),
    to_connection('10th','11th'),
    to_connection('11th','12th'),
    to_connection('12th','13th'),
    to_connection('13th','14th'),
    to_connection('14th','15th'),
    to_connection('15th','16th'),
    to_connection('16th','out'),

    to_connection('5th_1', '6th_1'),
    to_connection('6th_1', '7th_1'),
    to_connection('7th_1', '8th_1'),
    to_connection('8th_1', '9th_1'),
    to_connection('9th_1', '10th_1'),
    to_connection('10th_1', '11th_1'),
    to_connection('11th_1', '12th_1'),
    to_connection('12th_1', '13th_1'),
    to_connection('13th_1', '14th_1'),
    to_connection('14th_1', '15th_1'),
    to_connection('15th_1', '16th_1'),
    to_connection('16th_1', 'out_1'),

    to_connection('9th_2', '10th_2'),
    to_connection('10th_2', '11th_2'),
    to_connection('11th_2', '12th_2'),
    to_connection('12th_2', '13th_2'),
    to_connection('13th_2', '14th_2'),
    to_connection('14th_2', '15th_2'),
    to_connection('15th_2', '16th_2'),
    to_connection('16th_2', 'out_2'),

    to_connection('13th_3', '14th_3'),
    to_connection('14th_3', '15th_3'),
    to_connection('15th_3', '16th_3'),
    to_connection('16th_3', 'out_3'),

    # first split
    to_connection('4th','5th_1'),

    # second split
    to_connection('8th_1','9th_2'),
    to_connection('8th_1','9th'),
    to_connection('8th','9th_2'),
    to_connection('8th','9th_1'),

    # third split
    to_connection('12th_1','13th_2'),
    to_connection('12th_1','13th'),
    to_connection('12th_1','13th_3'),
    to_connection('12th','13th_1'),
    to_connection('12th','13th_2'),
    to_connection('12th','13th_3'),
    to_connection('12th_2','13th'),
    to_connection('12th_2','13th_1'),
    to_connection('12th_2', '13th_3'),

    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
