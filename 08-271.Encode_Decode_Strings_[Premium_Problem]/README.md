659 · Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhang104）


Examples

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"


##### My notes

- It would be nice if we could store the length of each word somewhere but that is not allowed. So instead, we could store the length of the string in the encoded string itself along with a delimiter like # 
- So we could say that when we encounter a number and a hash, then it means we have a string of length of that number next to #

For example, 

```python
input_str = ["lint","code","love","you"]
encoded = "4#lint4#code4#love3#you"
```
Now we could easily traverse this encoded string and see, 
- when we hit a number followed by #, then we can traverse that number amount of characters and add it to an array

