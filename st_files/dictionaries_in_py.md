##  **`Dictionaries in Python`**

##### Dictionary in python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds the `key:value pair`. Key-value is provided in the dictionary to make it more optimized. 

![Dict](https://www.digitalvidya.com/wp-content/uploads/2019/03/Image-3-4.png)

- In Dictionary each key is separated from its value by a colon `(:)`, the items are separated by `commas`, and the whole thing is enclosed in `curly braces`. 
- An empty dictionary without any items is written with just two curly braces, like this `{}`.
- Indexing of Python Dictionary is done with the help of `keys`. These are of any `hashable type` i.e. an object whose can never change like strings, numbers, tuples, etc.

### `Properties of Dictionary : ` 

- #### `Ordered` 
As of Python version 3.7, dictionaries are ordered, it means that the items have a defined order, and that order will not change.

- #### `Changeable`
we can change, add or remove items after the dictionary has been created.

- #### `Duplicates Not Allowed`
Dictionaries cannot have two items with the same key. If Duplicates exist, then they will overwrite the existing values.


### `Example : `

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(type(thisdict))
print(len(thisdict))
```

#### `Output : `

```
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Ford
<class 'dict'>
4
```