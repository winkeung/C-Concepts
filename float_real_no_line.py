# number line length and position
no_line_length = 2000
x_offset = 10
y_offset = 50
exp_mark_height = 50
fraction_mark_height = 20

# floating point bits length
exp_bit_len = 3
fraction_bit_len = 4

def print_line(x1,x2,y1,y2,id,stroke):
    print("<line fill=\"none\" id=\"" + id +"\" stroke=\"" + stroke + "\" x1=\"" + str(x1) + "\" x2=\"" + str(x2) +"\" y1=\"" + str(y1) + "\" y2=\"" + str(y2) + "\"/>")

# ratio: the ratio of the lenght of number line 1 = full length
def print_exp_mark(ratio):
    print_line(
        x_offset + no_line_length * ratio,
        x_offset + no_line_length * ratio,
        y_offset - exp_mark_height/2, 
        y_offset + exp_mark_height/2, "mark_exp", "#000000")

# ratio: the ratio of the lenght of number line 1 = full length
def print_fraction_mark(ratio):
    print_line(
        x_offset + no_line_length * ratio,
        x_offset + no_line_length * ratio,
        y_offset - fraction_mark_height/2, 
        y_offset + fraction_mark_height/2, "mark_fract", "#0000FF")


def print_no(ratio, text):
    print("<text fill=\"#000000\" font-family=\"serif\" font-size=\"13\" id=\"svg_1\" stroke=\"#0000ff\" stroke-width=\"0\" text-anchor=\"middle\" x=\"" + str(x_offset+ratio*no_line_length) + "\" xml:space=\"preserve\" y=\"19.21666\">" + text + "</text>")


print_line(x_offset, x_offset + no_line_length, y_offset, y_offset, "line", "#000000")
for i in range(2**exp_bit_len):
    if (i == 2**exp_bit_len-1): # the last division extend to zero point
        print_exp_mark(0)
        print_no(0, "0")
        for j in range(2**fraction_bit_len):
            print_fraction_mark(1/(2**(i-1))*(1/2**fraction_bit_len)*j)
    else:        
        print_exp_mark(1/(2**i))
        print_no(1/(2**i), "2^"+str(8-i-4))
        if (i != 0):
            for j in range(2**fraction_bit_len):
                print_fraction_mark(1/(2**i)+1/(2**i)*(1/2**fraction_bit_len)*j)
