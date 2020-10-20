# simple_progress_bar
I made this cute little progress before I discovered tqdm.<br>
It's a good friend if for some reason you can't afford 
another dependency.

## Usage:

* Copy the function into your code (wherever convenient for you)
* Provide the function with the current index and total length (Best to put it in the loop :P)

## Example:
```python
for i in range(10):
  #do stuff
  progress(i, 10)
  ```
