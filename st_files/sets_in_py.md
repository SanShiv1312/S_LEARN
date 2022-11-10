### `Sets in Python` 

##### Sets are a collection of unordered elements that are unique. Sets are used to store multiple items in a single variable.
##### Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference. 

![sets](https://www.freecodecamp.org/news/content/images/2019/12/image-65.png)

- The sets in python are typically used for mathematical operations like union, intersection, difference and complement etc.
- The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.

### `Properties of Sets : ` 

- #### `Unordered`
It means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

- #### `Unchangeable`
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

- #### `Duplicates Not Allowed`
Sets cannot have two items with the same value.


#### `set() and add() methods`
Python set() method is used for type casting in Python

```
myset = set(["a", "b", "c"])
print(myset)
 
# Adding element to the set
myset.add("d")
print(myset)
```
##### Output :

```
{'a', 'b', 'c'}
{'a', 'b', 'c', 'd'}
``` 

#### `Union operation on Sets` 
Two sets can be merged using `union()` function or `|` operator.

```
a = {"1","2","3"}
b = {"x"}
c = a.union(b)
print(c)
```
##### Output :

```
{'1', '3', '2', 'x'}
```
- In the similar way, we can perform `Intersection`, `Difference` and `Clear` operations on given input.
