import unittest
from BACK.conections.arangodb import ID_userdb
from unittest.mock import Mock, patch

class TestConect(unittest.TestCase):
    @patch('ConectDB.DataBase.tables')
    def test_tables(self,mock_db):
        mock_db.return_value=['tabla1','tabla2','tabla3']
        
        db=DataBase(DSN="user=postgres password=guirales123 host=localhost port=5432 dbname=postgres")
        
        result =db.tables()
        self.assertEqual(result, ['tabla1','tabla2','tabla3'])
        self.assertEqual(mock_db.call_count,1)
    

if __name__=="__main__":
    #python3 -m unittest -v tests/Test_ConectDB.py 
    unittest.main()