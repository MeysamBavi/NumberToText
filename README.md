# NumberToText

A python module to convert number to text

## Introduction

This module contains necessary object models for understanding and implementing a number to text system.  
The default implementation is for the English language and decimal number system, but you can easily extend these models to any language and number system you want; even the smallest details can be modified.

## Example

You can run `example.py` to test the module and its efficiency.

## How does it work?

### DigitSetConverter

When trying to read numbers, we usually separate digits into groups with a certain length; like *thousand*, *million* etc. which are 3 digits each. This grouping logic is the base of this module's system.  
First we separate the digits into these groups (or `sets`) and then connect the result of each set using `NumberToText` object. But how do things work in `DigitSetConverter`?  
Well, there are **3** ways we could have a name for the digit or the number. We start from the left hand side - the most significant digit - to the right side:
+ First we check if the resulting substring (from that position in the left to right of the number), has a specific name; e.g. *eleven* for `11`. If it has, we have our result. The digits themselves like `3` are converted this way.
+ If not, we check if that digit in that position, has a specific name; e.g. `2` in the second position from the right is always *twenty*. If it has a name, we are **only** done with **that digit**.
+ And finally if none of the ways above work, these *must* be a multiplier name for that position, so we can attach it to a digit; e.g. the third position from the right is always *hundred* and `300` is read *three hundred* (a digit attached to a multiplier).

You can look up the `dict` variables in `digit_set.py` to see these three ways. Obviously all of them can be overridden by you!  
It's also good to know that *zeros* in any position are ignored in this process.

### NumberToText

As said above, we separate the digits into groups (or `sets`) and then connect the result of each set using `NumberToText` object.  
Depending on how far left that set has been, there is a multiplier name for that; e.g. *thousand*, *million* etc. (the exception is the first set that has no multiplier). This multiplier comes after the text of the digit set in the resulting string; e.g. *twenty thousand* for `20000`.  

### Formatter

The `Formatter` object is responsible for converting the list of strings you get from `raw_convert`. All the necessary variables like space, comma and even the word '*and*' itself are stored in this object.  
By default, the `format` method `joins` all of the items in an iterable but the last one with a comma, and then joins the last one with the word '*and*'.  
`stick_last_two` is a tricky method, in a sense that it is only used sometimes. It basically does what it suggests: It sticks the last two items in the list and then `format`s them with the rest. It comes in handy when we don't want `144` to be converted to '*one hundred, forty and four*' (which is what `format` does) instead of '*one hundred and forty four*'.  

## Outro

Thank you for reading. The door is open for any suggestions :)
