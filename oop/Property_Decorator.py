class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property
  def age_in_days(self):     # اي فنكشن جوا كلاس بتاخذ بس سيلف ممكن نحولها لبروبارتي 

    return self.age * 365

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hello())
# print(one.age_in_days())

print(one.age_in_days)
