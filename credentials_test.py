import unittest 
import pyperclip
import random
import string 
from credentials import Credential
from user import User

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''

    def setUp(self):
      '''
      Setup method to run before each test cases
      '''
      self.new_credential = Credential('Machel','youtube','jkl54')

    def test_init(self):
       '''
       test_init checks if the object is initialised properly
       '''
       self.new_credential.username, ("Machel")
       self.new_credential.password, ("mk12")

    def tearDown(self):
       '''
        TearDown method that does clean up after each test case has run.
       '''
       Credential.credential_list = []

    def test_save_credential(self):
       '''
       test_save_credential tests if a new credential has been added to the credential_list 
       '''
       self.new_credential.save_credential()
       facebook = Credential("Frank", "Facebook","klj")
       facebook.save_credential()
       self.assertEqual(len(Credential.credential_list), 2)

    def test_display_credential(self):
       '''
       test to display the credentials
       '''
       self.new_credential.save_credential()
       youtube = Credential("Machel","youtube","jkl54")
       youtube.save_credential()
       youtube = Credential('Machel','youtube','jkl54')
       youtube.save_credential()
       self.assertEqual(len(Credential.display_credential(youtube.username)), 1)
       
    def test_find_by_sitename(self):
        '''
        Test case to test if we can search credential by sitename and return the correct credential.
        '''

        self.new_credential.save_credential()
        youtube = Credential('Machel','youtube','jkl54')
        youtube.save_credential()
        credential_exists = Credential.find_by_sitename('youtube')
        self.assertEqual(credential_exists, youtube)


   #  def test_delete_credential(self):
   #     '''
   #     test_delete_contact to test if we can remove a password from our credentials
   #     '''
   #     self.new_credential.save_credential()
   #     test_credential = ("Test","user","mk12")
   #     test_credential.save_credential()

   #     self.new_credential.delete_credential()
   #     self.assertEqual(len(Credential.credential_list),1)
    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_credential.save_credential()
        credential_exist = Credential.credential_exist('sitename')
        return credential_exist

    def test_copy_credential(self):
        '''
        Test case to test if the copy credential function copies the correct credential.
        '''
        self.new_credential.save_credential()
        youtube = Credential('Machel','youtube','jkl54')
        youtube.save_credential()
        find_credential = None
        for credential in Credential.credential_list:
            find_credential = Credential.find_by_sitename(credential.sitename)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.sitename)
        self.assertEqual('jkl54', pyperclip.paste())
        print(pyperclip.paste())  
  

if __name__ == '__main__':
     unittest.main() 
           