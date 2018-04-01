import src

class TestHelloWorld(unittest.TestCase):
	"""Test the 'hello_world' function from src"""
	
	def setUp(self):
		self.hello_msg = "Hello, World!"
	
	def test_prints_hello_world(self):
		output = src.hello_world()
		assert(output == self.hello_msg)