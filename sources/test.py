from unittest import runner
from unittest.main import main
from engine import Note
import unittest


class TestNote(unittest.TestCase):

    def test_list(self):
        Note.note_list.append('test')
        self.assertIn('test', Note.note_list)
        Note.note_list.clear()

    def test_add(self):
        Note.add('test')
        self.assertIn('test', Note.note_list)
        Note.note_list.clear()

    def test_edit(self):
        Note.note_list.append('test')
        Note.edit(1, 'test2')
        self.assertIn('test2', Note.note_list)
        Note.note_list.clear()

    def test_delete(self):
        Note.note_list.append('test')
        Note.delete(1)
        self.assertNotIn('test', Note.note_list)
        Note.note_list.clear()

    def test_check(self):
        self.assertEqual(Note.check(), 0)
        Note.note_list.append('test')
        Note.check()
        self.assertEqual(Note.check(), 1)
        Note.note_list.clear()

if __name__ == '__main__':
    
    import xmlrunner
    run=xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=run)
    unittest.main()
