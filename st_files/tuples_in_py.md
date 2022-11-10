##  **`Tuples in Python`**

##### Python Tuple is a collection of Python objects much like a list but Tuples are immutable in nature i.e. the elements in the tuple cannot be added or removed once created. Just like a List, a Tuple can also contain elements of various types.

##### Tuples are `immutable`, and usually contain a `heterogeneous` sequence of elements
- In Python, tuples are created by placing a sequence of values separated by `comma` with or without the use of parentheses for grouping of the data sequence
- Tuple items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

![tuples](https://imgur.com/gkH3N4I.png)

### `Example : `

```
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
```

#### `Output : `

```
('apple', 'banana', 'cherry')
3
```

- Tuples can also allow duplicate entries or elements since they are indexed.
- Tuples are relatively faster than lists, cause they are immutable.

### `Properties of Tuples` 

- #### `Ordered`
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

- #### `Unchangeable`
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

- #### `Allow Duplicates`
Since tuples are indexed, they can have items with the same value:

