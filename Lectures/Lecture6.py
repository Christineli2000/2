
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')


# ----------------------------------------------------------------------------
#   Opening the `SRCFILE` and reading its contents with the read method
# ----------------------------------------------------------------------------
# This will open the file located at `SRCFILE` and return a handler (file
# object):
fobj  = '?'

# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts  = '?'

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
#print(cnts[:20])

# Check if the file is closed
#print(fobj.closed)

# Close the file
#fobj.close()
#print(fobj.closed)

# ----------------------------------------------------------------------------
#   Comparing different approaches to get the contents
# ----------------------------------------------------------------------------
# Remember that we previously closed the file so we need to open it again
#fobj = open(SRCFILE, mode='r')
# Contents using `.read`
#cnts = fobj.read()
#print(f"First 20 characters in cnts: '{cnts[:20]}'")

# Start with an empty string
#cnts_copy = ''
# Iterate over each line of fobj # <comment>
#for line in fobj:
    # Add this line to the string `cnts_copy` # <comment>
#    cnts_copy += line

# Print the result
#print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")

# close the file
#fobj.close()


# ----------------------------------------------------------------------------
#   Reading one line at a time
# ----------------------------------------------------------------------------
#fobj = open(SRCFILE, mode='r')

# Read the first line
#first_line = next(fobj)

# After that, the fobj iterator now points to the second line in the file

#for line in fobj:
#    print(f"fobj now point to : '{line}'")
#    break
#

# close the file
#fobj.close()


# ----------------------------------------------------------------------------
#   Using context managers
# ----------------------------------------------------------------------------
# Instead of fobj = open(SRCFILE, mode='r'), use a context manager:

#with open(SRCFILE, mode='r') as fobj:
#    cnts = fobj.read()
#    # Check if the object is closed inside the manager
#    print(f'Is the fobj closed inside the manager? {fobj.closed}')
#

# Notice that we did not close the object when using a context manager
# But after exiting the context manager, the file will automatically close
#print(f'Is the fobj closed after we exit the manager? {fobj.closed}')



# ----------------------------------------------------------------------------
#   Writing content to a file
# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")


#  This will create the file located at `DSTFILE` and write some content to it

#with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line')
#

# Exiting the context manager will close the file
# We can then print its contents
#print_lines(DSTFILE)


# If you open the same file again in writing mode, the line we wrote above
# will be erased:

#with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is another line')
#
#print_lines(DSTFILE)
#



# ----------------------------------------------------------------------------
#   The write method does not add terminate the line.
# ----------------------------------------------------------------------------

#with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line')
#    fobj.write('This is a another line')
#print_lines(DSTFILE)
#

# ----------------------------------------------------------------------------
#   Notice that the write method does not add a newline character (\n). You
#   must add it yourself:
# ----------------------------------------------------------------------------

#with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
#print_lines(DSTFILE)
#


# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
# ----------------------------------------------------------------------------
def print_lines_rstrip(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")

#
#with open(DSTFILE, mode='w') as fobj:
#    fobj.write('This is a line\n')
#    fobj.write('This is a another line')
#print_lines_rstrip(DSTFILE)
#


# ----------------------------------------------------------------------------
#   Quiz: Create the save_open function here
# ----------------------------------------------------------------------------
def safe_open(pth, mode):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
    """
    pass
