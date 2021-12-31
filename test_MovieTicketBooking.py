import unittest
import MovieTicketBooking

class TestBooking(unittest.TestCase):
    def test_username(self):
        username = "prajakta"
        result = MovieTicketBooking.username()
        self.assertEqual(username, result, msg='Incorrect Password!')
     
    def test_password(self):
        password = "Rutuja"
        result = MovieTicketBooking.password()
        self.assertEqual(password, result, msg='Incorrect Password!')
    
    def test_city(self):
        result = MovieTicketBooking.city()
        self.assertTrue(0<result<4, msg='Incorrect City Choice!')
      
    def test_theatre(self):
        result = MovieTicketBooking.theatre()
        self.assertTrue(0<result<4, msg='Incorrect Theatre Choice!') 
      
    def test_movie(self):
        result = MovieTicketBooking.movie()
        self.assertTrue(0<result<4, msg='Incorrect Movie Choice!')
    
    def test_screen(self):
        result = MovieTicketBooking.screen()
        self.assertTrue(0<result<4, msg='Incorrect Screen Choice!')
        
    
        
if __name__ == '__main__':
        unittest.main()