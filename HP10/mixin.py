# mixin
# This file contains a mixin class that provides a method to convert a string to a list of words.
# The mixin class is called StringTolistMixin and it has a method called string_to_list.
# The string_to_list method takes a string as input and returns a list of words in the string.
# the mixin class is used to add functionality to another class without modifyting the orginal class.
# This ALLOWS for code reuse and better organization.
class StringTolistMixin:
    def string_to_list(self, string):
        """convert a string to a list of words"""
        return string.split()


class Test(StringTolistMixin):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string_to_list(self.string)


t1 = Test("hello world ")
print(t1.__str__())
