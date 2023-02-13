#!/usr/bin/python3
from time import sleep
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel

""" Defines tests /test cases for the base_model module <base_model.py> """


class TestBaseModelClass(unittest.TestCase):
    """ Defines a class with BaseModel test cases """

    def setUp(self):
        """ set up BaseModel object(s) to use in tests """
        self.base = BaseModel()

    # test class instantiates (doesn't require parameters)
    def test_class_instantiation(self):
        """ test class instantiation """
        base1 = BaseModel()
        self.assertEqual(type(base1), type(self.base))

    # test all public attributes are assigned
    def test_attributes_assigment_on_instantiation(self):
        """ test class instantiation assigns id, created
        and updated_at attributes """
        attrs = ['created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertTrue(attr in self.base.__dict__)

    # test that id's are unique
    def test_object_id_unique(self):
        """ test class objects have ubique ids """
        base1 = BaseModel()
        self.assertFalse(base1.id == self.base.id)

    # test that id is converted to string (from uuid type)
    def test_object_id_isStr(self):
        """ test that object id is converted to string """
        self.assertTrue(type(self.base.id) is str)

    # test that created_at and updated_at are !equal on object creation
    def test_creation_and_update_time_different_at_creation(self):
        """ test that object creation and update time is NOT the same
        at creation/ instantiation """
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    # test that save actually updates the last updated_at value)
    def test_save(self):
        """ test that the save instance method updates updated_at  """
        base1 = BaseModel()
        old_time = base1.updated_at
        base1.save()
        self.assertNotEqual(old_time, base1.updated_at)

    # test the str method
    def test_str_method(self):
        """ test class' str method """
        '''
        class_str = "[BaseModel] (a5ea90ac-b061-4f0e-a4d1-e40802e2bd2e)
                     {'id': 'a5ea90ac-b061-4f0e-a4d1-e40802e2bd2e',
                     'created_at': datetime.datetime(2022, 11, 22, 14, 40, 16,
                     131513), 'updated_at': datetime.datetime
                     (2022, 11, 22, 14, 40, 16, 131518)}"
        '''
        # self.assertEqual(len(class_str), len(str(self.base)))
        self.assertTrue(len(str(self.base)) > 100)

    # test the to_dict method
    def test_to_dict(self):
        """ test that the to_dict instance method returns a dictionary """
        self.assertTrue(type(self.base.to_dict()) is dict)

    # test that the datetime objects are converted into str
    def test_to_dict_datetime_is_str(self):
        """ test that the to_dict instance method converts datetime
        objects to strings its return dict """
        cls_dict = self.base.to_dict()
        self.assertTrue('datetime' not in cls_dict.values() and
                        type(cls_dict['created_at']) is str)

    # test that the __class__ key is appended to the dict (in to_dict)
    def test_to_dict_class_key(self):
        """ test that the to_dict instance method adds the __class__
        key (with class name value) to its return dict """
        cls_dict = self.base.to_dict()
        self.assertTrue('__class__' in cls_dict.keys())

    # test that the __class__ key's value is 'BaseModel'
    def test_to_dict_class_key_value(self):
        """ test that the to_dict the __class__ key's value
        is the class_name """
        cls_dict = self.base.to_dict()
        self.assertEqual(cls_dict['__class__'], 'BaseModel')


class TestBaseModelRecreation(unittest.TestCase):
    """ Defines tests for the BaseModel, recreation """

    def setUp(self):
        """ initialize a class to use in tests """
        self.base = BaseModel()
        self.base.name = 'Test_Model'
        self.base.number = 7
        obj_dict = self.base.to_dict()
        self.new_base = BaseModel(**obj_dict)

    # test that kwargs are checked for before initializing new objects
    def test_object_recreation_kwargs_check(self):
        """ test that kwargs are checked for before initializing
        new objects i.e. if provided, they are used """
        attrs = {'name': 'Test'}
        base1 = BaseModel(**attrs)
        self.assertTrue('name' in (base1.__dict__).keys())

    # test that datetime strings are converted back to datetime
    def test_object_recreation_datetime_conversion(self):
        """ test that datetime strings are converted back to
        datetime objects """
        self.assertTrue(isinstance(self.new_base.created_at, datetime))

    # test that without kwargs, normal initialization occurs
    def test_object_recreation_no_kwargs(self):
        """ test that if **kwargs isn't defined, normal
        initialization occurs """
        self.assertTrue(self.base)

    # test that args are not used
    def test_object_recreation_args_not_used(self):
        """ test that if **kwargs isn't defined, normal
        initialization occurs, args aren't used """
        args = ['Test_Model', 'hello']
        base1 = BaseModel(*args)
        for arg in args:
            # assert that potential attributes (args) dont exist
            self.assertEqual(getattr(self, arg, None), None)

    # test that a __class__ attribute isn't added
    def test_object_recreation_args__class__handled(self):
        """ test that if **kwargs is defined, the __class__
        key/value is not added as an attribute """
        self.assertTrue(getattr(self.new_base, '__class__', None), None)


"""
A test suite for BaseModel
"""


class TestBaseModel(unittest.TestCase):
    """
    Contains series of test cases for BaseModel class
    """

    def test_if_id_attribute_is_present(self):
        """
        Checks if BaseModel has the id attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'id'))

    def test_if_created_at_attribute_is_present(self):
        """
        Checks if the BaseModel has the created_at attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_if_updated_at_attribute_is_present(self):
        """
        Checks if the BaseModel has the updated_at attribute
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_if_id_is_unique(self):
        """
        Checks if id attribute is unique
        """
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_if_id_is_str(self):
        """
        Checks if id is a string
        """
        a = BaseModel()
        self.assertTrue(type(a.id), str)

    def test_if_str_has_correct_output(self):
        """
        Checks if __str__ has appropriate output
        """
        a = BaseModel()
        self.assertEqual(str(a), f"[BaseModel] ({a.id}) {a.__dict__}")

    def test_if_to_dict_returns_dict(self):
        """
        Checks if to_dict method returns a dict
        """
        a = BaseModel()
        self.assertTrue(type(a.to_dict()), dict)

    def test_if_key_class_is_in_dict(self):
        """Checks if the key __class__ is in o.to_dict"""
        a = BaseModel()
        self.assertIn('__class__', a.to_dict())

    def test_if_created_at_is_datetime_object(self):
        """Checks if created_at is a datetime obj """
        a = BaseModel()
        self.assertTrue(type(a.created_at), datetime)

    def test_if_updated_at_is_datetime_object(self):
        """Checks if updated_at is a datetime obj"""
        a = BaseModel()
        self.assertTrue(type(a.updated_at), datetime)

    def test_if_created_at_and_updated_at_is_same_initially(self):
        """Tests if created_at & updated_at attr have same values
        initially"""
        a = BaseModel()
        self.assertEqual(a.created_at, a.updated_at)

    def test_two_objects_created_at(self):
        """Compares the created_at time of two class instances"""
        a = BaseModel()
        sleep(0.2)
        b = BaseModel()
        self.assertLess(a.created_at, b.created_at)

    def test_if_save_method_updates_updated_at_attr(self):
        """Checks if calling save method updated the updated_at attr"""
        a = BaseModel()
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)
        self.assertGreater(a.updated_at.microsecond, a.created_at.microsecond)


if __name__ == "__main__":
    unittest.main()
