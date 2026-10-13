import unittest

from fastapi.testclient import TestClient

from fast_note.app import app, get_note_snapshot, notes


class NotesApiTests(unittest.TestCase):
    def setUp(self):
        notes.clear()
        self.client = TestClient(app)
        self.addCleanup(self.client.close)
        self.addCleanup(notes.clear)

if __name__ == "__main__":
    unittest.main()
