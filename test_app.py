import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import db_drop_and_create_all, setup_db, Movie, Actor


class castingAgencyTestCase(unittest.TestCase):
    """This class represents the casting_agency test case"""


    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        user = os.environ.get('POSTGRES_USER')
        password = os.environ.get('POSTGRES_PASSWORD')
        self.database_path = "postgresql://{}:{}@{}/{}".format(user,password,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.assistant_token = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVzVi1MWTNBVjhxakVDTkNCT3NmdyJ9.eyJpc3MiOiJodHRwczovL2Rldi16NnJzNnBzNy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOGZmMDA2MzI2MWEwMDY4N2JhMWJhIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MzE0NzQ0ODMsImV4cCI6MTYzMTU2MDg4MywiYXpwIjoiVkI0cVFCZTZ6eU80R2VYc2NOOTkyTzhybkhrd2JNS1YiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.RR2V93U3-NEXw0s3O87_l-P4ItVLnkL_boutmedCcYHdYJhjLT7zNh-RViAwZ_A9p1dJCHi121X55H9V1Jgi8abCf8zfDWLxbs7uenRY3cLmt81-qGiJ2xB5UdseqQmSAlHP1V8WVj3w-292rzrX6DFHEOGeDwv0zrQg_m0kaosrU9fd8RzGYeBAYFxMIrT0saYgVJg1jCJvRx_Mu4bAsTpMqH2_z48SfjevYLeVYRZHDKNuQK_y51ukNpn5TEV5YyGSspRkWM3-ACDWJHwYQeTdVohkFHkGoqzkzbK95ErA_ODEcrC8aSnNS4scmA6RkjakKVOFwXQn-ayZF4US1Q'
        self.director_token =  'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVzVi1MWTNBVjhxakVDTkNCT3NmdyJ9.eyJpc3MiOiJodHRwczovL2Rldi16NnJzNnBzNy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYjg5NmE2MzI2MWEwMDY4N2MzZjk5IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MzE0NzQ2OTcsImV4cCI6MTYzMTU2MTA5NywiYXpwIjoiVkI0cVFCZTZ6eU80R2VYc2NOOTkyTzhybkhrd2JNS1YiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiXX0.vnKuqOmVlG3_YDAeg2rksLiS5wFW8ToiOACL5RLH9PyqsM1LUftJ2hFjq5AILeqqTU5UXrAdZne4tDl9j52cQdrHVEK5xg2OHfOFCCNQ-3o6ZIxvwv7V2fuTxGdwk2iJr-dhXqW2EyX0IMA5KXz0_rB8qIHsWiBKAqH_Qf-F3JndoZJgRpd3x6snELWfRkWgK3PnJirP1nCLg-RImxq9sbe1shuvHtMXjr9V141s0xtgm7NinUbX0eTNDhmTqgqDE7qm70PP4MAO5st4noH1fHOWuP4e6YC0lW-tGwCYLumIln53jnRnkAO4FzNXo0Y-7ZJVs3pIWQxUNf4UoFHJeg'
        self.executive_token = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVzVi1MWTNBVjhxakVDTkNCT3NmdyJ9.eyJpc3MiOiJodHRwczovL2Rldi16NnJzNnBzNy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYmEwYmU0ZmVjNmQwMDY4MmIxN2Q1IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MzE0NzQ1MzcsImV4cCI6MTYzMTU2MDkzNywiYXpwIjoiVkI0cVFCZTZ6eU80R2VYc2NOOTkyTzhybkhrd2JNS1YiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyJdfQ.ieGoqD-Q2Zg3m3R8R34T2oOD5M8DlMOsj4moRog1Cd9z_H-JWhxrUyBQsBbdUza7nX6OIzMKF9lFvfh527nhhzKU1uzRrQid2z5g5s3ATnnuhc-XFM8B2tg6SCNTG_ye7GP8Iz-kos3u-_saOJOZ5FC9rJ8ra3eAgKrceockUBex1Xy4Kvo8g3X3CG_DWgG5_fByddXDwzGE3SGfxxOJ-SCw3avAPVBVhiRbt3zwstA1aO0KwywT8oAticcCGivn3VsqoIer2-f6QxCEzYo8lC7x0zkGYqnKFZCX9r9qy3dotK83pIXNUJHid6J1Lyy8Rd0e_oegxsZPH8kKENQP6g'

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    
    def tearDown(self):
        """Executed after reach test"""
        db_drop_and_create_all()
        
    
    #Test Cases for Route: /actors
    
    # Method: get
    
    #1- suceessful request

    def test_get_actors(self):
        res = self.client().get('/actors', headers={'Authorization': self.assistant_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    #2- Failed request , 401
    
    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    
    #Method: Post

    #1- Successful 
    def test_create_actor(self):
        res = self.client().post('/actors',
         headers={'Authorization': self.director_token},
         json={'name':'Mohammed', 'age': 20, 'gender':'Male'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
    
    #2- Failed request, 422
    def test_422_create_actor(self):
        res = self.client().post('/actors', headers={'Authorization': self.director_token},
        json={'name':'', 'age':'', 'gender':''})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)

    #Method: Patch

    #1- Successful
    def test_patch_actor(self):
        res = self.client().patch('/actors/1', headers={'Authorization': self.director_token},
        json={'name':'Mohammed', 'age': 22, 'gender':'Male'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
    
    #2- Failed request, 404
    def test_404_patch_actor(self):
        res = self.client().patch('/actors/1000', headers={'Authorization': self.director_token},
        json={'name':'Mohammed', 'age': 20})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)
    
    #Method: Delete

    #1- Successful
    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers={'Authorization': self.director_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
    
    #2- Failed request
    def test_404_delete_actor(self):
        res = self.client().delete('/actors/1000', headers={'Authorization': self.director_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    
    #Test cases for Route: /movies 
    
    #Method: get

    #1- Successful request
    def test_get_movies(self):
        res = self.client().get('/movies', headers={'Authorization': self.director_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
    
    #2- Failed request, 401
    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)

    #Method: Post

    #1- Successful request
 
    def test_create_movie(self):
        res = self.client().post('/movies',
         headers={'Authorization': self.executive_token},
         json={'title':'Joker', 'release date': '2019-5-6'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
    
    #2- Failed request, 422
    def test_422_create_movie(self):
        res = self.client().post('/actors', headers={'Authorization': self.executive_token},
        json={'title':'', 'release date':''})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)

    #Method: Patch

    #1- Successful
    def test_patch_movie(self):
        res = self.client().patch('/movies/1', headers={'Authorization': self.director_token},
        json={'title':'The dark knight', 'release date': '2008-9-5'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
    
    #2- Failed request, 404
    def test_404_patch_movie(self):
        res = self.client().patch('/movies/1000', headers={'Authorization': self.director_token},
        json={'title':'The dark knight', 'release date': '2008-9-5', 'gender':'Male'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)
    
    #Method: Delete

    #1- Successful
    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers={'Authorization': self.executive_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
    
    #2- Failed request
    def test_404_delete_movie(self):
        res = self.client().delete('/movies/1000', headers={'Authorization': self.executive_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    

    # RBAC Test cases

    #1- Casting Assistant

    # Authorized operation: get:movies
    def test_assistant_permession_success(self):
        res = self.client().get('/movies', headers={'Authorization': self.assistant_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    #Unauthorized operation: patch:movies
    def test_assistant_permession_failure(self):
        res = self.client().patch('/movies/1', headers={'Authorization': self.assistant_token},
        json={'title':'The dark knight', 'release date': '2008-9-5', 'gender':'Male'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)
    
    #2- Casting Director
        # Authorized operation: get:movies
    def test_director_permession_success(self):
        res = self.client().get('/movies', headers={'Authorization': self.director_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    #Unauthorized operation: delete:movies
    def test_director_permession_failure(self):
        res = self.client().delete('/movies/1', headers={'Authorization': self.director_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)
    
    #3- Executive Producer
        # Authorized operation: create:movies
    def test_executive_permession_success(self):
        res = self.client().post('/movies',
         headers={'Authorization': self.executive_token},
         json={'title':'Lier Lier', 'release date': '2005-5-6'})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
    #Authorized operation: delete:movies
    def test_executive_permession_success_2(self):
        res = self.client().delete('/movies/1', headers={'Authorization': self.executive_token})
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
if __name__ == "__main__":
    unittest.main()