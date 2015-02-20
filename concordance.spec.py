#!/usr/bin/python
# coding: utf-8

import unittest
import book
import concordance


class TestConcordance(unittest.TestCase):

    def setUp(self):
        self.test_book = book.Book(
            'An excerpt from Hamlet',
            [
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
When we have shuffled off this mortal coil,''',
                '''Must give us pause. There's the respect
That makes calamity of so long life.''',
                '''For who would bear the whips and scorns of time,
Th' oppressor's wrong, the proud man's contumely,''',
                '''The pangs of despis'd love, the law's delay,
The insolence of office, and the spurns''',
                '''That patient merit of th' unworthy takes,
When he himself might his quietus make''',
                '''With a bare bodkin? Who would these fardels bear,
To grunt and sweat under a weary life,''',
                '''But that the dread of something after death-
The undiscover'd country, from whose bourn''',
                '''No traveller returns- puzzles the will,
And makes us rather bear those ills we have''',
                '''Than fly to others that we know not of?
Thus conscience does make cowards of us all,''',
                '''And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,''',
                '''And enterprises of great pith and moment
With this regard their currents turn awry''',
                '''And lose the name of action.- Soft you now!
The fair Ophelia!- Nymph, in thy orisons''',
                '''Be all my sins rememb'red.'''
              ]
        )

        self.test_book_concordance_data = {
            "'Tis": set([4]),
            "'tis": set([1]),
            'And': set([3, 15, 16, 17]),
            'Be': set([18]),
            'But': set([12]),
            'Devoutly': set([5]),
            'For': set([6, 8]),
            'Must': set([7]),
            'No': set([13]),
            'Nymph': set([17]),
            'Ophelia': set([17]),
            'Soft': set([17]),
            'Than': set([14]),
            'That': set([10]),
            'The': set([2, 4, 9]),
            "There's": set([7]),
            'To': set([1, 3, 5]),
            'Who': set([11]),
            'With': set([11]),
            'a': set([2, 3, 4, 11]),
            'action': set([17]),
            'after': set([12]),
            'against': set([2]),
            'all': set([14, 18]),
            'and': set([2, 3, 4, 8, 9, 11, 16]),
            'arms': set([2]),
            'arrows': set([2]),
            'awry': set([16]),
            'ay': set([5]),
            'bare': set([11]),
            'be': set([1, 5]),
            'bear': set([8, 13]),
            'bearTo': set([11]),
            'bodkin': set([11]),
            'bourn': set([12]),
            'by': set([3]),
            'calamity': set([7]),
            'cast': set([15]),
            'coil': set([6]),
            'comeWhen': set([6]),
            'conscience': set([14]),
            'consummation': set([4]),
            'contumely': set([8]),
            'country': set([12]),
            'cowards': set([14]),
            'currents': set([16]),
            'death': set([6]),
            'deathThe': set([12]),
            'delayThe': set([9]),
            "despis'd": set([9]),
            'die': set([3, 5]),
            'does': set([14]),
            'dread': set([12]),
            'dream': set([5]),
            'dreams': set([6]),
            'end': set([3]),
            'enterprises': set([16]),
            'fair': set([17]),
            'fardels': set([11]),
            'flesh': set([4]),
            'fly': set([14]),
            'fortuneOr': set([2]),
            'from': set([12]),
            'give': set([7]),
            'great': set([16]),
            'grunt': set([11]),
            'have': set([6, 13]),
            'he': set([10]),
            'heartache': set([4]),
            'heir': set([4]),
            'himself': set([10]),
            'his': set([10]),
            'hue': set([15]),
            'ills': set([13]),
            'in': set([1, 6, 17]),
            'insolence': set([9]),
            'is': set([1, 4]),
            'know': set([14]),
            "law's": set([9]),
            'life': set([7, 11]),
            'long': set([7]),
            'lose': set([17]),
            'love': set([9]),
            'make': set([10, 14]),
            'makes': set([7, 13]),
            "man's": set([8]),
            'may': set([6]),
            'merit': set([10]),
            'might': set([10]),
            'mind': set([1]),
            'momentWith': set([16]),
            'more': set([3]),
            'mortal': set([6]),
            'my': set([18]),
            'name': set([17]),
            'native': set([15]),
            'natural': set([4]),
            'nobler': set([1]),
            'not': set([1, 14]),
            'nowThe': set([17]),
            "o'er": set([15]),
            'of': set([2, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17]),
            'ofThus': set([14]),
            'off': set([6]),
            'office': set([9]),
            'opposing': set([3]),
            "oppressor's": set([8]),
            'or': set([1]),
            'orisons': set([17]),
            'others': set([14]),
            'outrageous': set([2]),
            'pale': set([15]),
            'pangs': set([9]),
            'patient': set([10]),
            'pause': set([7]),
            'perchance': set([5]),
            'pith': set([16]),
            'proud': set([8]),
            'puzzles': set([13]),
            'questionWhether': set([1]),
            'quietus': set([10]),
            'rather': set([13]),
            'regard': set([16]),
            "rememb'red": set([18]),
            'resolutionIs': set([15]),
            'respectThat': set([7]),
            'returns': set([13]),
            'rub': set([5]),
            'say': set([3]),
            'scorns': set([8]),
            'sea': set([2]),
            'shocksThat': set([4]),
            'shuffled': set([6]),
            'sicklied': set([15]),
            'sins': set([18]),
            'sleep': set([3, 5, 6]),
            'sleepNo': set([3]),
            'sleepTo': set([5]),
            'slings': set([2]),
            'so': set([7]),
            'something': set([12]),
            'spurns': set([9]),
            'suffer': set([1]),
            'sweat': set([11]),
            'take': set([2]),
            'takesWhen': set([10]),
            "th'": set([10]),
            'that': set([1, 6, 12, 14]),
            'the': set([1, 4, 5, 7, 8, 9, 12, 13, 15, 17]),
            'their': set([16]),
            'them': set([3]),
            "there's": set([5]),
            'these': set([11]),
            'this': set([6, 16]),
            'those': set([13]),
            'thought': set([15]),
            'thousand': set([4]),
            'thus': set([15]),
            'thy': set([17]),
            "timeTh'": set([8]),
            'to': set([1, 2, 3, 4, 5, 14]),
            'traveller': set([13]),
            'troubles': set([2]),
            'turn': set([16]),
            'under': set([11]),
            "undiscover'd": set([12]),
            'unworthy': set([10]),
            'us': set([7, 13, 14]),
            'we': set([3, 6, 13, 14]),
            'weary': set([11]),
            'what': set([6]),
            'whips': set([8]),
            'who': set([8]),
            'whose': set([12]),
            'willAnd': set([13]),
            "wish'd": set([5]),
            'with': set([15]),
            'would': set([8, 11]),
            'wrong': set([8]),
            'you': set([17])
        }

        self.simple_book = book.Book(
            'A very simple book',
            [
                'Apple Banana',
                'Apple',
                'Apple Zebra',
                '',
                'Banana'
            ]
        )

        self.simple_book_concordace_data = {
            'Apple': set([1,2,3]),
            'Banana': set([1,5]),
            'Zebra': set([3])
        }

    def test_concordance(self):
        self.assertEqual.__self__.maxDiff = None
        test_book_concordance = concordance.Concordance(self.test_book)
        self.assertEqual(
            self.test_book_concordance_data,
            test_book_concordance.__dict__['concordance']
        )

    def test_simple_concordance(self):
        test_simple_concordance = concordance.Concordance(self.simple_book)
        self.assertEqual(
            self.simple_book_concordace_data,
            test_simple_concordance.__dict__['concordance']
        )


if __name__ == '__main__':
    unittest.main()

