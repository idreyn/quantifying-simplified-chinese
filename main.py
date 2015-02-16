#!/usr/bin/python
# -*- coding: utf-8 -*

from shentan.shentan import Shentan, CSVDict
from disorder import *

class StrokeCountDict(CSVDict):
  def __init__(self):
    for this, prev in super(StrokeCountDict,self).__init__(
      filename='../data/strokes.csv',
      keys=['unicode','strokes'],
      delimiter=' ',
      key_index=0
    ):
      self.entries[this][1] = int(self.entries[this][1])

shared_sh = False
shared_sc = False

def char_stroke_counts(num_chars=5000,sh=None,sc=None,isolate_simplifications=False):
  global shared_sh
  global shared_sc
  if not sh:
    if not shared_sh:
      shared_sh = Shentan()
    sh = shared_sh
  if not sc:
    if not shared_sc:
      shared_sc = StrokeCountDict()
    sc = shared_sc
  simp_char_strokes = []
  trad_char_strokes = []
  simp_actually_simplified = []
  trad_actually_simplified = []
  for i in xrange(0,num_chars):
    simp_char = sh.knowledge.characters.entry_by_index(i)[1]
    if not sc.entry(simp_char):
      continue
    simp_strokes = sc.entry(simp_char)['strokes']
    trad_char = sh.jianti_to_fanti(simp_char)
    trad_strokes = sc.entry(trad_char)['strokes']
    if simp_char != trad_char:
      simp_actually_simplified.append(simp_strokes)
      trad_actually_simplified.append(trad_strokes)
    simp_char_strokes.append(simp_strokes)
    trad_char_strokes.append(trad_strokes)
  if isolate_simplifications:
    return simp_char_strokes, trad_char_strokes, simp_actually_simplified, trad_actually_simplified
  else:
    return simp_char_strokes, trad_char_strokes

