import unittest
import sys
import os

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models import Patient

class PatientsTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_add_patient(self):
        with app.app_context():
            new_patient = Patient(
                year=2024,
                given_name="John",
                surname="Doe",
                sex="M",
                dob="1990-01-01",
                current_location="123 Main St",
                city="Port Moresby",
                nationality="PNG"
            )
            db.session.add(new_patient)
            db.session.commit()

            self.assertEqual(Patient.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
