#!/usr/bin/python
# coding: utf-8

import unittest
import book
import concordance


class TestConcordance(unittest.TestCase):

    def setUp(self):
        self.test_book = book.Book([
            '''To be, or not to be- that is the question:
Whether 'tis nobler in the mind to suffer''',
            '''The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles,''',
            '''And by opposing end them. To die- to sleep-
No more; and by a sleep to say we end''',
            '''The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation''',
            '''Devoutly to be wish'd. To die- to sleep.
To sleep- perchance to dream: ay, there's the rub!''',
            '''For in that sleep of death what dreams may come
When we have shuffled off this mortal coil, ''',
            '''Must give us pause. There's the respect
That makes calamity of so long life.''',
            '''For who would bear the whips and scorns of time,
Th' oppressor's wrong, the proud man's contumely,''',
            '''The pangs of despis'd love, the law's delay,
The insolence of office, and the spurns''',
            '''That patient merit of th' unworthy takes,
When he himself might his quietus make''',
            '''With a bare bodkin? Who would these fardels bear,
To grunt and sweat under a weary life, ''',
            '''But that the dread of something after death-
The undiscover'd country, from whose bourn''',
            '''No traveller returns- puzzles the will,
And makes us rather bear those ills we have''',
            '''Than fly to others that we know not of?
Thus conscience does make cowards of us all,''',
            '''And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,''',
            '''And enterprises of great pith and moment
With this regard their currents turn awry ''',
            '''And lose the name of action.- Soft you now!
The fair Ophelia!- Nymph, in thy orisons''',
            '''Be all my sins rememb'red.'''
        ])
        self.test_book_concordance_data = {
            '\'tis': set([0, 3]),
            'a': set([1, 2, 3, 10]),
            'action': set([16]),
            'after': set([11]),
            'against': set([1]),
            'all': set([13, 17]),
            'and': set([1, 2, 3, 7, 8, 10, 14, 15, 16]),
            'arms': set([1]),
            'arrows': set([1]),
            'awry': set([15]),
            'ay': set([4]),
            'bare': set([10]),
            'be': set([0, 4, 17]),
            'bear': set([7, 12]),
            'bearto': set([10]),
            'bodkin': set([10]),
            'bourn': set([11]),
            'but': set([11]),
            'by': set([2]),
            'calamity': set([6]),
            'cast': set([14]),
            'coil': set([5]),
            'comewhen': set([5]),
            'conscience': set([13]),
            'consummation': set([3]),
            'contumely': set([7]),
            'country': set([11]),
            'cowards': set([13]),
            'currents': set([15]),
            'death': set([5]),
            'deaththe': set([11]),
            'delaythe': set([8]),
            'despis\'d': set([8]),
            'devoutly': set([4]),
            'die': set([2, 4]),
            'does': set([13]),
            'dread': set([11]),
            'dream': set([4]),
            'dreams': set([5]),
            'end': set([2]),
            'enterprises': set([15]),
            'fair': set([16]),
            'fardels': set([10]),
            'flesh': set([3]),
            'fly': set([13]),
            'for': set([5, 7]),
            'fortuneor': set([1]),
            'from': set([11]),
            'give': set([6]),
            'great': set([15]),
            'grunt': set([10]),
            'have': set([5, 12]),
            'he': set([9]),
            'heartache': set([3]),
            'heir': set([3]),
            'himself': set([9]),
            'his': set([9]),
            'hue': set([14]),
            'ills': set([12]),
            'in': set([0, 5, 16]),
            'insolence': set([8]),
            'is': set([0, 3]),
            'know': set([13]),
            'law\'s': set([8]),
            'life': set([6, 10]),
            'long': set([6]),
            'lose': set([16]),
            'love': set([8]),
            'make': set([9, 13]),
            'makes': set([6, 12]),
            'man\'s': set([7]),
            'may': set([5]),
            'merit': set([9]),
            'might': set([9]),
            'mind': set([0]),
            'momentwith': set([15]),
            'more': set([2]),
            'mortal': set([5]),
            'must': set([6]),
            'my': set([17]),
            'name': set([16]),
            'native': set([14]),
            'natural': set([3]),
            'no': set([12]),
            'nobler': set([0]),
            'not': set([0, 13]),
            'nowthe': set([16]),
            'nymph': set([16]),
            'o\'er': set([14]),
            'of': set([1, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16]),
            'off': set([5]),
            'office': set([8]),
            'ofthus': set([13]),
            'ophelia': set([16]),
            'opposing': set([2]),
            'oppressor\'s': set([7]),
            'or': set([0]),
            'orisons': set([16]),
            'others': set([13]),
            'outrageous': set([1]),
            'pale': set([14]),
            'pangs': set([8]),
            'patient': set([9]),
            'pause': set([6]),
            'perchance': set([4]),
            'pith': set([15]),
            'proud': set([7]),
            'puzzles': set([12]),
            'questionwhether': set([0]),
            'quietus': set([9]),
            'rather': set([12]),
            'regard': set([15]),
            'rememb\'red': set([17]),
            'resolutionis': set([14]),
            'respectthat': set([6]),
            'returns': set([12]),
            'rub': set([4]),
            'say': set([2]),
            'scorns': set([7]),
            'sea': set([1]),
            'shocksthat': set([3]),
            'shuffled': set([5]),
            'sicklied': set([14]),
            'sins': set([17]),
            'sleep': set([2, 4, 5]),
            'sleepno': set([2]),
            'sleepto': set([4]),
            'slings': set([1]),
            'so': set([6]),
            'soft': set([16]),
            'something': set([11]),
            'spurns': set([8]),
            'suffer': set([0]),
            'sweat': set([10]),
            'take': set([1]),
            'takeswhen': set([9]),
            'th\'': set([9]),
            'than': set([13]),
            'that': set([0, 5, 9, 11, 13]),
            'the': set([0, 1, 3, 4, 6, 7, 8, 11, 12, 14, 16]),
            'their': set([15]),
            'them': set([2]),
            'there\'s': set([4, 6]),
            'these': set([10]),
            'this': set([5, 15]),
            'those': set([12]),
            'thought': set([14]),
            'thousand': set([3]),
            'thus': set([14]),
            'thy': set([16]),
            'timeth\'': set([7]),
            'to': set([0, 1, 2, 3, 4, 13]),
            'traveller': set([12]),
            'troubles': set([1]),
            'turn': set([15]),
            'under': set([10]),
            'undiscover\'d': set([11]),
            'unworthy': set([9]),
            'us': set([6, 12, 13]),
            'we': set([2, 5, 12, 13]),
            'weary': set([10]),
            'what': set([5]),
            'whips': set([7]),
            'who': set([7, 10]),
            'whose': set([11]),
            'willand': set([12]),
            'wish\'d': set([4]),
            'with': set([10, 14]),
            'would': set([7, 10]),
            'wrong': set([7]),
            'you': set([16])
        }

        self.simple_book = book.Book([
            'Apple Banana',
            'Apple',
            'Apple Zebra',
            '',
            'Banana'
        ])

        self.simple_book_concordace_data = {
            'Apple': [1,2,3],
            'Banana': [1,5],
            'Zebra': [3]
        }

    def test_concordance(self):
        test_book_concordance = concordance.Concordance(self.test_book)
        self.assertEqual(
            test_book_concordance_data,
            test_book_concordance.__dict__['corcordance']
        )

    def test_simple_concordance(self):
        test_simple_concordance = concordance.Concordance(self.simple_book)
        self.assertEqual(
            self.simple_book_concordace_data,
            test_simple_concordance.__dict__['corcordance']
        )


if __name__ == '__main__':
    unittest.main()

