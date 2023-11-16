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
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
""" week9_slides_groups_and_bools.py

Codes discussed in class during Week 9

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ week9/
    |   |   |__ __init__.py                         <- Required (empty file)
    |   |   |__ week9_slides_groups_and_bools.py    <- This module
    |   |
    |   |__ lec_utils.py                        <- Required
    |       ...
    |__ toolkit_config.py


"""
import pandas as pd

from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False


# ----------------------------------------------------------------------------
#  Create the event data frame
# ----------------------------------------------------------------------------
def mk_rec_df0(show: bool = False):
    """ Creates an example DF

    Parameters
    ----------
    show: bool, optional
        If True, print DF

    Returns
    -------
    data frame :

                                     firm   action  event_date
        date
        2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
        2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
        2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
        2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
        2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 7 entries, 2012-02-16 07:42:00 to 2020-12-09 15:34:34
        Data columns (total 3 columns):
        #   Column      Non-Null Count  Dtype
        ---  ------      --------------  -----
        0   firm        7 non-null      object
        1   action      7 non-null      object
        2   event_date  7 non-null      object

    """
    cnts_rec_csv = '''
    date                , firm           , action
    2012-02-16 07:42:00 , JP Morgan      , main
    2020-09-23 08:58:55 , Deutsche Bank  , main
    2020-09-23 09:01:26 , Deutsche Bank  , main
    2020-09-23 09:11:01 , Wunderlich     , down
    2020-09-23 11:15:12 , Deutsche bank  , up
    2020-11-18 11:07:44 , Morgan Stanley , up
    2020-12-09 15:34:34 , JP Morgan      , main
    '''
    df = utils.csv_to_df(cnts_rec_csv, index_col='date', parse_dates=['date'])

    # Upper case version of 'firm' column
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()

    # Create a string with the date part of the DatetimeIndex
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    if show is True:
        utils.pprint(df, "Example DF:")
    return df


def groupby_example0():
    """ Example illustrating groupby as a Slit-Apply-Combine operation

    In this example, we will split the DF into groups defined by the
    value of Firm
    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0(show=True)

    # Output:
    #
    # date                           firm action  event_date
    # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
    # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # Suppose we want to select the last rec for each firm (only)

    # Split into groups by firms

    # date                           firm action  event_date
    # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # date                           firm action  event_date
    # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

    # date                           firm action  event_date
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

    # date                           firm action  event_date
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Apply the operation "select last obs"

    # date                           firm action  event_date
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # date                           firm action  event_date
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

    # date                           firm action  event_date
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

    # date                           firm action  event_date
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Combine the result

    # date                           firm action  event_date
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # ----------------------------------------------------------------------------
    #   Creating groupby objects
    # ----------------------------------------------------------------------------
    groups = '?'
    # <example>
    # groups = df.groupby('firm')
    # </example>
    utils.pprint(groups, "df.groupby('firm')")

    # ----------------------------------------------------------------------------
    # The attribute "GroupBy.groups" -> Dict with groups
    # ----------------------------------------------------------------------------
    obj = '?'
    # <example>
    # groups = df.groupby('firm')
    # obj= groups.groups
    # </example>
    utils.pprint(obj, "groups.groups:", )

    # Output:
    # {'DEUTSCHE BANK': DatetimeIndex(['2020-09-23 08:58:55', '2020-09-23 09:01:26', '2020-09-23 11:15:12'],
    #                   dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'JP MORGAN': DatetimeIndex(['2012-02-16 07:42:00', '2020-12-09 15:34:34'],
    #                   dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'MORGAN STANLEY': DatetimeIndex([ '2020-11-18 11:07:44'],
    #                     dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'WUNDERLICH': DatetimeIndex(['2020-09-23 09:11:01'],
    #                     dtype='datetime64[ns]', name='date', freq=None)
    #  }

    # ----------------------------------------------------------------------------
    #   The elements of groups.groups
    # ----------------------------------------------------------------------------
    # <example>
    # df = mk_rec_df0()
    # groups = df.groupby(by='firm')
    # for firm, idx in groups.groups.items():
    #    group_df = df.loc[idx]
    #    utils.pprint(group_df, msg=f"Data for Firm == '{firm}':", show_type=False)
    # </example>

    # ----------------------------------------------------------------------------
    #   Applying functions to individual groups
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    # <example>
    ## First, using a loop:
    ##
    ## Task: Create a dictionary with the number of observations
    ## for each value of "firm"
    # dic = {}
    # for firm, idx in groups.groups.items():
    #    nobs = len(df.loc[idx])
    #    print(f"Number of obs for Firm == '{firm}' is {nobs}")
    #    dic[firm] = nobs
    ##utils.pprint(dic, "This is dic:\n")
    # </example>

    # Then using the apply method
    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    res = '?'
    # <example>
    # res = groups.apply(len) # <mask>
    # </example>
    utils.pprint(res, "groups.apply(len):\n")

    # You can apply your own functions
    def get_last(df):
        """ Sorts the dataframe on its index and returns
            last row of the sorted dataframe
        """
        df.sort_index(inplace=True)
        return df.iloc[-1]

    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    res = '?'
    # <example>
    # res = groups.apply(get_last) # <mask>
    # <example>
    utils.pprint(res, "groups.apply(get_last):\n")

    # Some group by operations are so common that Pandas implements them directly
    # on any created instance of `GroupBy`. Here are some examples:
    #
    # - `GroupBy.count`: count observations per group (exclude missing values)
    # - `GroupBy.size`: get group size, i.e., count observations per group (including missing values)
    # - `GroupBy.last`: select last of observation in each group

    # Count the number of observations inside each group:
    # (includes missing values if any)
    df = mk_rec_df0()
    groups = df.groupby('firm')
    res = '?'
    # <example>
    # res = groups.count()
    # </example>
    utils.pprint(res, "groups.count():\n")

    # Select last obs by group
    df = mk_rec_df0()
    groups = df.groupby('firm')
    res = '?'
    # <example>
    # res = df.groupby('firm').last() # <mark>
    # </example>
    utils.pprint(res, "df.groupby('firm').last():\n")


def groupby_example1():
    """ Grouping using multiple columns
    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    utils.pprint(df, "This is df:")

    # Split the data into groups
    groups = '?'
    # <example>
    # groups = df.groupby(['firm', 'event_date']) # <mask>
    # </example>
    utils.pprint(groups, "df.groupby(['firm', 'event_date']):\n")

    # Select the most recent obs for each group
    res = '?'
    # <example>
    # res = groups.last()
    # </example>
    utils.pprint(res, "groups.last():")

    # The index of the new DF is a MultiIndex
    obj = '?'
    # <example>
    # obj = res.index
    # </example>
    utils.pprint(obj, "The res.index:\n")

    # Converting the index to columns

    # <example>
    # df = mk_rec_df0()
    # df.sort_index(inplace=True)
    # groups = df.groupby(['firm', 'event_date'])
    # res = groups.last()
    # utils.pprint(res,  "res:\n")
    # new_df = res.reset_index()
    # utils.pprint(new_df,  "res.reset_index():\n")
    # </example>


# ----------------------------------------------------------------------------
#   New topic: Selecting using booleans
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#   New example DF
# ----------------------------------------------------------------------------
def mk_rec_df1():
    """ Creates an example DF

    Returns
    -------
    data frame :

         event_date            firm action
      0  2012-02-16       JP MORGAN   main
      1  2020-09-23   DEUTSCHE BANK     up
      2  2020-09-23      WUNDERLICH   down
      3  2020-11-18  MORGAN STANLEY     up
      4  2020-12-09       JP MORGAN   main

      <class 'pandas.core.frame.DataFrame'>
      RangeIndex: 5 entries, 0 to 4
      Data columns (total 3 columns):
       #   Column      Non-Null Count  Dtype
      ---  ------      --------------  -----
       0   event_date  5 non-null      object
       1   firm        5 non-null      object
       2   action      5 non-null      object

    """
    # --------------------------------------------------------
    # Start with the example df and keep only the last rec
    # by a given firm on a given day
    # --------------------------------------------------------
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    groups = df.groupby(['event_date', 'firm'])
    df = groups.last().reset_index()
    return df


def bool_example0():
    """ Given a DF with the last rec for each firm/event-day, keep only
    upgrades and downgrades

    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df1()
    utils.pprint(df, "This is df:\n")

    # ----------------------------------------------------------------------------
    #   Using booleans to select rows
    # ----------------------------------------------------------------------------
    # will be a series with boolean values
    cond = '?'
    # <example>
    # cond = df.loc[:, 'action'] == 'up'
    # </example>
    utils.pprint(cond, "cond = df.loc[:, 'action'] == 'up'\nThen cond is:\n")

    # We can use this series as an indexer:
    # A series of booleans can be used to select rows that meet the criteria
    res = '?'
    # <example>
    # res = df.loc[cond] # <mask>
    # </example>
    utils.pprint(res, "df.loc[cond]:\n")

    # ----------------------------------------------------------------------------
    #   Using booleans to select rows and cols
    # ----------------------------------------------------------------------------
    col_cond = [False, True, False]
    res = '?'
    # <example>
    # res = df.loc[:, col_cond] # <mask>
    # utils.pprint(df, "This is df:\n")
    # </example>
    utils.pprint(res, f"The output of df.loc[:, {col_cond}] is:\n")

    # ----------------------------------------------------------------------------
    #   Multiple criteria
    # ----------------------------------------------------------------------------
    # Combine different criteria
    res = '?'
    # <example>
    # crit = (df.loc[:, 'action'] == 'up') | (df.loc[:, 'action'] == 'down')
    # res = df.loc[crit]
    # </example>
    utils.pprint(res, "df.loc[crit]")

    # ----------------------------------------------------------------------------
    #   Using the `str.contains` method
    # ----------------------------------------------------------------------------
    crit = '?'
    # <example>
    # crit = df.loc[:, 'action'].str.contains('up|down') # <mask>
    # res = df.loc[crit]
    # </example>
    utils.pprint(res, "df.loc[:, 'action'].str.contains('up|down'):\n")


def mk_event_df0():
    """ Example showing how to create the column "event_type"
    This is df:

    Given the following DF

       event_date            firm action
    1  2020-09-23   DEUTSCHE BANK     up
    2  2020-09-23      WUNDERLICH   down
    3  2020-11-18  MORGAN STANLEY     up

    This example produces:

                        firm  event_date event_type
    event_id
    1          DEUTSCHE BANK  2020-09-23    upgrade
    2             WUNDERLICH  2020-09-23  downgrade
    3         MORGAN STANLEY  2020-11-18    upgrade

    """
    # Start with the recs and keep only upgrades/downgrades
    df = mk_rec_df1()
    crit = df.loc[:, 'action'].str.contains('up|down')  # <mask>
    df = df.loc[crit]
    utils.pprint(df, "This is df:\n")

    # ----------------------------------------------------------------------------
    #  Create a column called event_type
    # ----------------------------------------------------------------------------
    event_df = df.copy()

    def _et(value):
        if value == 'up':
            return 'upgrade'
        elif value == 'down':
            return 'downgrade'
        else:
            raise Exception(f"value must be either 'up' or 'down'")

    event_df.loc[:, 'event_type'] = event_df.loc[:, 'action'].apply(_et)
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>

    # ----------------------------------------------------------------------------
    #  Keep only the columns of interest
    # ----------------------------------------------------------------------------
    cols = ['firm', 'event_date', 'event_type']
    event_df = event_df.loc[:, cols]
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>

    # ----------------------------------------------------------------------------
    #  Add the index
    # ----------------------------------------------------------------------------
    event_df.reset_index(inplace=True, drop=True)
    event_df.index = event_df.index + 1
    event_df.index.name = 'event_id'
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>
    return event_df


def apply_example0():
    """ How to use the data frame method apply
    """
    # Example DF
    df = mk_event_df0()
    df.loc[:, 'event_type'] = df.event_type.str.upper()
    utils.pprint(df, "df:")

    # apply
    res = df.apply(max)
    utils.pprint(res, "df.apply(max)")

    # what if we want "row-wise"?

    res = df.apply(max, axis=1)
    utils.pprint(res, "df.apply(max, axis=1)")

    def sel_lower(ser, pos):
        """ Replace the element at position `pos` with lowercase
        """
        ser.iloc[pos] = ser.iloc[pos].lower()
        return ser

    res = df.apply(sel_lower, pos=0)
    utils.pprint(res, "df.apply(sel_lower, pos=0)")


if __name__ == "__main__":
    # Example DF
    # df = mk_rec_df0(show=True)

    # groupby_example0()
    # groupby_example1()

    # bool_example0()
    # mk_event_df0()

    # apply_example0()

    pass
