
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
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
""" week8_slides_p1.py

Codes discussed in class during Week 7, Part 1: the datetime module

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ __init__.py             <- Required (empty file)
    |   |__ lec_utils.py            <- Required
    |   |
    |   |__ week8/
    |   |   |__ __init__.py             <- Required (empty file)
    |   |   |__ week8_slides_p1.py      <- This module
    |   |   |__ week8_slides_p2.py      
    |       ...
    |__ toolkit_config.py


I will talk about the `lec_utils.py` module during class

"""
import datetime as dt

from webinars import lec_utils as utils

# Set the options for this part of the lecture
# (all this does is to modify the behavior of pprint)
utils.pp_cfg.sep = True
utils.pp_cfg.show_type = True



# ----------------------------------------------------------------------------
# Notes about datetime and lec_utils
#
# The datetime module
#  - datetime.datetime --> class representing both date and time stamps
#  - datetime.timedelta --> class representing duration
#
# Note that we are importing datetime as dt.  This is useful so we do not
# confuse datetime (the module) with datetime.datetime (the class)
#
#
# Notes about lec_utils.pprint:
#  - The function pprint is not to be confused with the module pprint (I did
#    this on purpose to illustrate how useful namespaces can be).
#
#  - The only functions from lec_utils we will use are
#       lec_utils.pprint.
#       lec_utils.csv_to_df
#       lec_utils.csv_to_fobj
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# The datetime class:
#   Implements several methods to generate instances of `datetime`
#   representing a certain date
# ----------------------------------------------------------------------------

# One of the methods implemented by `dt.datetime` is called `now`, which
# returns an instance of `dt.datetime` representing the current date/time.

# Instance of `dt.datetime` with the current date/time
dt_now = '?'
# <solution>
#dt_now  = dt.datetime.now()
# </solution>


# Aside: How can we print a representation of an object?
#
# repr(obj):
#   Returns a string containing a printable representation of an object.
#   Typically, there is an attempt to return the string that would
#   generate an object with the same type and value
#
# str(obj):
#   Returns a string "version" of the object (typically an "informal" printable
#   representation of the object, not necessarily how the object was
#   constructed)
#

# Let's look at an example using `dt_now`
# First, str(obj)

# <example>
#print("str(dt.datetime.now()) is:")
#print(str(dt_now))
# </example>


# NOTE: print(obj) is the same as print(str(obj))
# This means that `obj` is converted to string before printing

# Now, using `repr(obj)`
# Note that `dt_now` is an instance of datetime.datetime
# <example>
#print("repr(dt.datetime.now()) is:")
#print(repr(dt_now))
# </example>


# NOTE: How does `lec_utils.pprint` represent objects?
# For non-string objects, set the parameter `pretty`:
#   If pretty = True -> will use `repr` (DEFAULT)
#   If pretty = False -> will use `str`

# Example:
# <example>
#dt_now  = dt.datetime.now()
#utils.pprint(dt_now, msg="This is dt_now (pretty=True)", pretty=True)
#utils.pprint(dt_now, msg="This is dt_now (pretty=False)", pretty=False)
# </example>



# dt_now is an instance of dt.datetime
# Let's take a look at this class using help(dt.datetime)

# <example>
#help(dt.datetime)
# </example>


# From the output above, we can see that instances of `datetime` store the
# date (year, month, day) and time (hour, minute, second, microsecond). You
# can access these attributes directly from the instance:
#
#   dt_now.day
#   dt_now.month
#   dt_now.year
#   dt_now.hour
#   dt_now.minute
#   dt_now.second
#   dt_now.microsecond



# ----------------------------------------------------------------------------
#   Creating datetime.datetime instances
# ----------------------------------------------------------------------------

# Create another datetime instance

dt0 = dt.datetime(
    year=2022,
    month=11,
    day=1,
    hour=8,
    minute=0,
    second=0,
    microsecond=0)

#utils.pprint(dt0, "dt0 is:\n", pretty=False)


# We do not need to specify all the parameters (year, month, day are required)
# Create a dt.datetime obj with year=2022, month=11, day=1
dt1 = '?'

# <solution>
#dt1 = dt.datetime(
#    year=2022,
#    month=11,
#    day=1,
#)
# </solution>

#utils.pprint(dt1, "dt1 is:\n", pretty=False)
#utils.pprint(dt1.year, 'dt1.year')
#utils.pprint(dt1.month, 'dt1.month')
#utils.pprint(dt1.day, 'dt1.day')
#utils.pprint(dt1.hour, 'dt1.hour')


# ----------------------------------------------------------------------------
#   `datetime.timedelta` objects
# ----------------------------------------------------------------------------
# Lets create two other datetime instances:
#   dt0 --> 2019-12-31 00:00:00
#   dt1 --> 2020-01-01 00:00:00
dt0  = '?'
dt1  = '?'

# <solution>
#dt0 = dt.datetime(year=2019, month=12, day=31)
#dt1 = dt.datetime(year=2020, month=1, day=1)
# </solution>

#utils.pprint(dt0, "dt0 is:\n", pretty=False)
#utils.pprint(dt1, "dt1 is:\n", pretty=False)


# Operations between datetime objects will return timedelta objects
delta  = '?'

# <solution>
#delta = dt1 - dt0
# </solution>

#msg = f"The operation:\n  {repr(dt1)} \n    - {repr(dt0)}\ngives:"
#utils.pprint(delta, msg=msg)

# Let's create another timedelta using
#
#  `start`: 2020-12-31 00:00:00
#  `end`  : 2020-12-31 12:00:00
#
start = dt.datetime(year=2020, month=12, day=31, hour=0)
end = dt.datetime(year=2020, month=12, day=31, hour=12)

# These two dates are 12 hours apart
new_delta =  end - start

msg = f'''Given:
    start: {start}
    end: {end}
then `new_delta` is:
'''
#utils.pprint(new_delta, msg, )


# Add 12 hours to some date
#   - `start` will be the starting date (same as above)
#   - `delta` will be a period of 12 hours (same as new_delta)
#   - `new_end` will be the ending date (same as `end` above)
delta  = '?'

# <solution>
#delta = dt.timedelta(hours=12)
# </solution>

# This is the new date
# <example>
#new_end = start + delta
# </example>

# <example>
#msg = f'''Given:
#    start: {repr(start)}
#    delta: {repr(delta)}
#If
#    new_end = start + delta
#
#then `repr(new_end)` is:
#    {repr(new_end)}
#
#and `str(new_end)` is:
#    {str(new_end)}
#'''
#utils.pprint(msg, show_type=True)
# </example>

# ----------------------------------------------------------------------------
#   Important note about attributes:
#   dt = datetime.datetime(...) -->
#       dt.year,
#       dt.month,
#       dt.day,
#       dt.seconds, ...
#   td = datetime.timedelta(...) -->
#       td.days ,
#       dt.seconds,
#       dt.microseconds
# ----------------------------------------------------------------------------
# For instance, consider the following timedelta

# <example>
#delta_2yr = dt.timedelta(days=365*2)
#utils.pprint(delta_2yr, "delta_2yr:\n")
# </example>


# ----------------------------------------------------------------------------
#   Exercises (5 mins each)
# ----------------------------------------------------------------------------
# 1. For how many seconds have you been alive?

# <solution>
bday = dt.datetime(1974, 11, 8, hour=8, minute=45)
dt_now = dt.datetime.now()
alive = dt_now - bday
# Here is how the timedelta attributes days and seconds work:
#  td.days --> Number of days in the interval
#  td.seconds--> Number of seconds on top of the days in the interval
#               ( 0 <= td.seconds < 86,400 secs)
# Alternative 1:
secs = (alive.days * 24 * 60 * 60) + alive.seconds
# Alternative 2: Use the METHOD total_seconds
#secs = alive.total_seconds()
res = f"I have been alive for {secs:,.0f} secs"
#utils.pprint(res)
# </solution>


# 2. How old will you be in 1,340 days

# <solution>
# Time: 5 mins
# First, compute the future date
days = 1340
future = dt.datetime.now() + dt.timedelta(days=days)
# Then, the time you have been alive (timedelta)
alive = future - bday
# Then, calculate the number of years
age = alive.days/365.
res = f"In {days} days, I'll be {age:.2f} years"
#utils.pprint(res)
# </solution>

# ----------------------------------------------------------------------------
#   The `strftime` method
#   Used to create strings representing dates (in different format)
# ----------------------------------------------------------------------------

# | Directive | Meaning                                                       | Example                  |
# |-----------|---------------------------------------------------------------|--------------------------|
# | %a        | Weekday as locale's abbreviated name.                         | Sun, Mon,...             |
# | %A        | Weekday as locale's full name.                                | Sunday, Monday,...       |
# | %w        | Weekday as a decimal number (Sunday=0,Saturday=6)             | 0, 1,..., 6              |
# | %d        | Day of the month as a zero-padded decimal number.             | 01, 02, …, 31            |
# | %b        | Month as locale's abbreviated name.                           | Jan, Feb,..., Dec        |
# | %B        | Month as locale's full name.                                  | January, February,...    |
# | %m        | Month as a zero-padded decimal number.                        | 01, 02, …, 12            |
# | %y        | Year without century as a zero-padded decimal number.         | 00, 01,..., 99           |
# | %Y        | Year with century as a decimal number.                        | 0001, 1999, 2013, 2014   |
# | %H        | Hour (24-hour clock) as a zero-padded decimal number.         | 00, 01, …, 23            |
# | %I        | Hour (12-hour clock) as a zero-padded decimal number.         | 01, 02, …, 12            |
# | %p        | Locale's equivalent of either AM or PM.                       | AM, PM                   |
# | %M        | Minute as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %S        | Second as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %j        | Day of the year as a zero-padded decimal number.              | 001, 002, …, 366         |
# | %U        | Week number of the year (Sunday as the first day of the week) | 00, 01, …, 53            |
# | %W        | Week number of the year (Monday as the first day of the week) | 00, 01, …, 53            |
# | %c        | Locale's appropriate date and time representation.            | Tue Aug 16 21:30:00 1988 |

# Create a datetime object representing
#   2020-12-31 00:00:00
# <example>
#date = dt.datetime(year=2020, month=12, day=31, hour=0)
#utils.pprint(date, "date is:")
# </example>

# Convert to a **string** with the following formats
#   2020-12-31
#   Dec 31, 2020
s1  = '?'
# <example>
#s1 = date.strftime('%Y-%m-%d')
# </example>
#print(s1)
s2  = '?'
# <example>
#s2 = date.strftime('%b %d, %Y')
# </example>
#print(s2)
